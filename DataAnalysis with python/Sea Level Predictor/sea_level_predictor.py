import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    df = df.drop(df.iloc[:, 2:], axis=1)  # Drop unused columns
    x = df.iloc[:, 0]
    y = df.iloc[:, 1]
    print(df.head())

    # Create scatter plot only
    plt.scatter(x, y, color="blue", marker="o", label="Input Data")
    # Create first line of best fit
    res = linregress(x, y)
    y_intercept = res.intercept
    slope = res.slope
    print("Slope: " + str(slope) + " Y Intercept: " + str(y_intercept))

    # y = mx + b
    x_pred: range = range(x[0], 2050, 1)
    y_future = slope * x_pred + y_intercept

    plt.plot(x_pred, y_future, color="red", label="Trend Line from all data")

    # Create second line of best fit
    df_modern = df[df["Year"] >= 2000]
    res_modern = linregress(df_modern)
    y_intercept_modern = res_modern.intercept
    slope_modern = res_modern.slope

    x_pred_modern = range(2000, 2050, 1)
    y_future_modern = slope_modern * x_pred_modern + y_intercept_modern

    plt.plot(x_pred_modern, y_future_modern, color="green", label="Trend Line from present data")

    # Add labels and title
    plt.title = "Rise in Sea Level"
    plt.xlabel = "Year"
    plt.ylabel = "Sea Level (inches)"
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    plt.show()
    return plt.gca()
