import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")
df = df.set_index("id")

# Add 'overweight' column
weight = df["weight"]
height_in_meters = df["height"] / 100  # It is in cm, but we convert to metre for easier calculation
BMI = weight / (height_in_meters ** 2)
df['overweight'] = (BMI > 25).astype(int)


# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df[["gluc", "cholesterol"]] = (df[["gluc", "cholesterol"]] > 1).astype(int)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])

    # Melt is like a Cartesian product. But only between the id_vars and the value_vars
    # If we have n data, then cardio will go from 1 to n and matches all with all cholesterol data from 1 to n
    # when it is done it will reset the cardio to 1 and then goes and matches all gluc data from 1 to n

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    #df_cat = None

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(df_cat, kind='count', x='variable', hue='value', col='cardio').set(ylabel='total').fig
    # Draws a categorical plot from the given dataFrame. It is separated by the ID_VARS so the cardio it is given in col
    # kind is count, so it counts up all the different values.
    # X= is the collective name of the values on the x-axis

    # Get the figure for the output
    #fig = None

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[df['ap_lo'] <= df['ap_hi']]
    df_heat = df_heat[df_heat['height'] >= df['height'].quantile(0.025)]
    df_heat = df_heat[df_heat['height'] <= df['height'].quantile(0.975)]
    df_heat = df_heat[df_heat['weight'] >= df['weight'].quantile(0.025)]
    df_heat = df_heat[df_heat['weight'] <= df['weight'].quantile(0.975)]


    # Calculate the correlation matrix
    corr = df_heat.corr() # corr as in correlation
    # In this figure everything is corralated with everything. Even with itself, and duplicates results. SHOULD FILTER

    # Generate a mask for the upper triangle
    mask = np.triu(corr)
    # the upper triangle mask places 0-es under the k-th diagonal

    # Set up the matplotlib figure
    fig, ax = plt.subplots()

    # Draw the heatmap with 'sns.heatmap()'
    ax = sns.heatmap(corr, mask=mask, annot=True, fmt='0.1f', square=True)

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
