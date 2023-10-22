import ipywidgets as widgets
from IPython.display import clear_output
import seaborn as sns
import matplotlib.pyplot as plt

def create_tab_widget(stock_data, returns):
    """
    Create a tabbed widget to display various plots and statistics.

    Args:
        stock_data (pd.DataFrame): Stock data.
        returns (pd.DataFrame): Returns data.

    Returns:
        widgets.Tab: Tab widget with various plots and statistics.
    """
    tab_titles = ['Max Close', 'Min Return', 'Max Return', 'Standard Deviation', 'Seaborn Pairplot', 'Return Plot Density', 'Return Plot Histogram']

    # Create tab widget
    tab = widgets.Tab()
    tab.children = []

    # Create tab content functions
    def plot_max_close(change):
        with max_close_widget:
            plt.figure(figsize=(12, 6))
            stock_data.xs(key='close', axis=1, level='Stock Info').max().plot()
            plt.title("Max Close")
            plt.show()

    def plot_min_return(change):
        with min_return_widget:
            plt.figure(figsize=(12, 6))
            returns.idxmin().plot()
            plt.title("Min Return")
            plt.show()

    def plot_max_return(change):
        with max_return_widget:
            plt.figure(figsize=(12, 6))
            returns.idxmax().plot()
            plt.title("Max Return")
            plt.show()

    def display_std_deviation(change):
        with std_deviation_widget:
            plt.figure(figsize=(12, 6))
            returns.std().plot()
            plt.title("Standard Deviation")
            plt.show()

    def display_pairplot(change):
        with seaborn_pairplot_widget:
            sns.pairplot(returns[1:])
            plt.show()

    def display_density_plot(change):
        with returns_plot_density:
            plt.figure(figsize=(12, 6))
            returns.plot.density()
            plt.title("Return Plot Density")
            plt.show()

    def display_histogram(change):
        with returns_plot_hist:
            plt.figure(figsize=(12, 6))
            returns.plot.hist(alpha=0.5)
            plt.title("Return Plot Histogram")
            plt.show()

    # Create tab content widgets
    max_close_widget = widgets.Output()
    min_return_widget = widgets.Output()
    max_return_widget = widgets.Output()
    std_deviation_widget = widgets.Output()
    seaborn_pairplot_widget = widgets.Output()
    returns_plot_density = widgets.Output()
    returns_plot_hist = widgets.Output()

    # Add tab content to children
    tab.children += (max_close_widget, min_return_widget, max_return_widget, std_deviation_widget, seaborn_pairplot_widget, returns_plot_density, returns_plot_hist)

    # Set tab titles
    for i, title in enumerate(tab_titles):
        tab.set_title(i, title)

    # Define tab content change event handlers
    tab.observe(plot_max_close, names='selected_index')
    tab.observe(plot_min_return, names='selected_index')
    tab.observe(plot_max_return, names='selected_index')
    tab.observe(display_std_deviation, names='selected_index')
    tab.observe(display_pairplot, names='selected_index')
    tab.observe(display_density_plot, names='selected_index')
    tab.observe(display_histogram, names='selected_index')

    return tab

def create_column_plot_widget(df):
    # Create an interactive function for plotting a selected column
    def plot_selected_column(selected_column):
        if selected_column:
            plt.figure(figsize=(12, 6))
            df[selected_column].plot.hist()
            plt.title(f'{selected_column} Histogram')
            plt.show()

    # Get the unique column names for the user to select
    column_names = list(df.columns)

    # Create a dropdown widget to select a column
    column_dropdown = widgets.Dropdown(
        options=column_names,
        description='Select Column:',
    )

    # Create an interactive widget
    interactive_plot = widgets.interactive(plot_selected_column, selected_column=column_dropdown)

    # Display the interactive widget
    return interactive_plot


def plot_stock_data_with_window(stock_data, user_ticker, start_date, window_size):
    tick_data = stock_data[user_ticker].sort_index()

    plt.figure(figsize=(12, 6))
    tick_data['close'].loc[start_date:].rolling(window=window_size).mean().plot(label=f'{window_size} Day Avg')
    tick_data['close'].loc[start_date:].plot(label=user_ticker + ' CLOSE')
    plt.legend()
    plt.title(f'{user_ticker} Stock Data')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.show()


