import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    df = df.drop(df.iloc[:, 2:], axis=1)
    print(df.head())

    # Create scatter plot
    plt.scatter(df.iloc[:, 0], df.iloc[:, 1])
    plt.show()
    # Create first line of best fit

    # Create second line of best fit

    # Add labels and title

    # Save plot and return data for testing (DO NOT MODIFY)
    # plt.savefig('sea_level_plot.png')
    return plt.gca()
