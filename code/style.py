import seaborn as sns
import matplotlib.pyplot as plt


UMCOLORS = [
        "#00274C", # Blue,
        "#FFCB05", # Maize
        "#9A3324", # Tappan Red
        "#D86018",  # Ross Orange
        "#75988d", # Rackham Green
        "#A5A508", # Wave Field Green
        "#00B2A9", # Taubman Teal
        "#2F65A7", # Arboretum Blue
        "#702082", # A2 Amethyst
        "#575294", # Matthaei Violet
        "#CFC096", # UMMA Tan
        "#9B9A6D", # Burton Tower Beige
    
]


SMALL_SIZE = 8
MEDIUM_SIZE = 10
BIGGER_SIZE = 12


def set_style():
    plt.style.use("bmh")

    plt.rc('font', size=SMALL_SIZE)          # controls default text sizes 
    plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
    plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE, dpi=150, autolayout=True)
    # fontsize of the figure title, default dpi, and tight layout

    sns.set_palette(UMCOLORS)
