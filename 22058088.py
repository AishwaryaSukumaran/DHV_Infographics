# Data Source : https://www.kaggle.com/datasets/iamsouravbanerjee/world-population-dataset

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("world_population.csv")

remove = ['Rank' , 'CCA3' ,'Capital' ]
df = df.drop(columns = remove)

df.rename(columns = {'Country/Territory' : "Country"} , inplace = True)

df.describe()


# Select numeric columns for summary statistics
numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns

# Calculate summary statistics using NumPy
summary_statistics = df[numeric_columns].agg([np.mean, np.median, np.std, np.min, np.max])


def fun1(df, ax=None):
    if ax is None:
        _, ax = plt.subplots(figsize=(6 , 3))

    # Sort the DataFrame by population in descending order
    df_sorted = df.sort_values(by='2022 Population', ascending=False)

    # Take the top 10 countries
    top_countries = df_sorted.head(10).copy()
    top_countries['Population Billion'] = top_countries['2022 Population'] / 1e9

    # Use seaborn barplot
    sns.barplot(data=top_countries, x='Population Billion', y='Country', palette='viridis', ax=ax)

    # Annotate each bar with population value
    for i, (index, row) in enumerate(top_countries.iterrows()):
        ax.text(row['Population Billion'] + 0.05, i, f"{row['Population Billion']:.2f}B",
                ha='left', va='center', fontsize=10, color='black', weight='bold')

    # Set title and labels
    ax.set_title('Top 10 Countries by 2022 Population with Population in Billion')
    ax.set_xlabel('2022 Population in Billion')
    ax.set_ylabel('Country')

def fun2(df, ax=None):
    if ax is None:
        _, ax = plt.subplots(figsize=(6,3))

    continent_percentage = df.groupby('Continent')['World Population Percentage'].sum()
    explode = [0.1 if continent == 'Asia' else 0 for continent in continent_percentage.index]

    ax.pie(continent_percentage, labels=None, autopct='%1.1f%%', startangle=90, explode=explode, colors=plt.cm.Set3.colors)

    ax.legend(labels=continent_percentage.index, title='Continents', loc='upper left', bbox_to_anchor=(1, 1))
    ax.set_title('World Population Percentage by Continent')

def fun3(df, ax=None):
    if ax is None:
        _, ax = plt.subplots(figsize=(6,3))

    df_sorted_growth_rate = df.sort_values(by='Growth Rate', ascending=False)
    top_countries_growth_rate = df_sorted_growth_rate.head(5)

    sns.barplot(data=top_countries_growth_rate, x='Growth Rate', y='Country', palette='viridis', ax=ax)
    ax.set_title('Top 5 Countries with Maximum Growth Rate')
    ax.set_xlabel('Growth Rate')
    ax.set_ylabel('Country')

def fun4(df, ax=None):
    if ax is None:
        _, ax = plt.subplots(figsize=(6,3))

    df_sorted_density_population = df.sort_values(by=['Density (per km²)', '2022 Population'], ascending=[True, False])
    top_countries_density_population = df_sorted_density_population.head(5)

    sns.barplot(data=top_countries_density_population, x='Country', y='Density (per km²)', hue='2022 Population', palette='viridis', ax=ax)
    ax.set_title('Top 5 Countries with Lowest Density and High Population')
    ax.set_xlabel('Country')
    ax.set_ylabel('Density (per km²)')
    ax.legend(title='2022 Population', bbox_to_anchor=(1, 1), loc='upper left')

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(25, 25))
fig.suptitle("Exploring Global Population Trends and Insights ", fontsize=42 , fontweight = "bold")
fig.set_facecolor('#FCE6C9')

fun1(df, ax=axes[0,0])
fun2(df, ax=axes[0,1])
fun3(df, ax=axes[1, 0])
fun4(df, ax=axes[1, 1])

# Add a common description
description = ("The bar chart reveals that China has the world's highest population, "
"standing at 1.43 billion, closely followed by India with 1.42 billion and the United States with 0.34 billion inhabitants."

"Analyzing the pie chart, we observe that the Asian continent contributes significantly to the global population, accounting for 59.2% of the world's inhabitants."

"According to the bar chart, Moldova exhibits the highest growth rate among the featured countries, with a notable 1.3% increase in population."

"The bar chart highlights Namibia as having a substantial population of 3,398,366, yet it maintains a low population density."
"This contrasts with Mongolia and Western Sahara, which also have low population densities despite their respective population sizes.")


# Add student information
student_info = (
    "     \n\nName :Aishwarya Sukumaran  "
    "     \nStudent ID : 22058088"
)

fig.text(0.5, 0.02, description, ha='center', va='center', fontsize=16, wrap=True)
fig.text(0.5, 0.1, student_info, ha='center', va='center', fontsize=16, wrap=True)



# Adjust layout and save the figure
plt.tight_layout(rect=[0, 0.1, 1, 0.95])
plt.savefig("22058088.png", dpi=300)



