import matplotlib.pyplot as plt
import seaborn as sns

def plot_histogram_distributions(df, col, bins):
    # Setting plotting style
    plt.style.use('seaborn-v0_8-whitegrid')

    # Plot
    plt.figure(figsize=(8, 4))
    sns.histplot(df[col], kde=True, bins=bins)
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()


def plot_count_distributions(df, col):
    # Setting plotting style
    plt.style.use('seaborn-v0_8-whitegrid')
    # Poisson plot
    plt.figure(figsize=(8, 5))
    sns.countplot(x=df[col], color='skyblue')

    # Rotate x-axis labels to vertical
    plt.xticks(rotation=90)

    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Number of Policyholders')
    plt.show()

def plot_pair_scatter_plot(df):
    sns.pairplot(df)
    plt.show()

