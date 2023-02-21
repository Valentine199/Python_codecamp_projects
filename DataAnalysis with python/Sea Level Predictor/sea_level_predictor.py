import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    df = df.drop(df.iloc[:, 2:], axis=1)
    x = df.iloc[:, 0]
    y = df.iloc[:, 1]
    print(df.head())

    # Create scatter plot only
    plt.scatter(x, y, color="blue", marker="o", label="Input Data")
    # Create first line of best fit
    res = linregress(x, y)

    yIntercept = res.intercept
    slope = res.slope
    print("Slope: " + str(slope) + " Y Intercept: " + str(yIntercept))

    # y = mx + b
    xPred = range(x[0], 2050, 1)
    yFuture = slope * xPred + yIntercept

    plt.plot(xPred, yFuture, color="red", label="Trend Line")
    plt.show()

    # Create second line of best fit
    dfModern = df[df["Year"] >= 2000]

    # Add labels and title

    # Save plot and return data for testing (DO NOT MODIFY)
    # plt.savefig('sea_level_plot.png')
    return plt.gca()
