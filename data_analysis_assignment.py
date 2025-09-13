import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris


def main():
    # Task 1: Load and Explore Dataset

    print("Loading dataset...")
    iris = load_iris()

    # Convert to DataFrame
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df["species"] = pd.Categorical.from_codes(iris.target, iris.target_names)

    # Display first few rows
    print("\nFirst 5 rows of the dataset:")
    print(df.head())

    # Dataset info
    print("\nDataset info:")
    print(df.info())

    # Check for missing values
    print("\nMissing values per column:")
    print(df.isnull().sum())

    # Clean dataset 
    df = df.dropna()

    
    # Task 2: Basic Data Analysis
    
    print("\nBasic statistics:")
    print(df.describe())

    print("\nMean values per species:")
    group_means = df.groupby("species").mean()
    print(group_means)

    # Observations
    print("\nObservations:")
    print("• Setosa flowers generally have smaller petal lengths and widths.")
    print("• Virginica species tend to have the largest petal measurements.")
    print("• Sepal length shows less variation across species compared to petal length.")

    
    # Task 3: Data Visualization
    
    # 1. Line Chart
    plt.figure(figsize=(8, 5))
    plt.plot(df.index, df["sepal length (cm)"], label="Sepal Length")
    plt.title("Line Chart: Sepal Length Across Samples")
    plt.xlabel("Sample Index")
    plt.ylabel("Sepal Length (cm)")
    plt.legend()
    plt.show()

    # 2. Bar Chart
    plt.figure(figsize=(8, 5))
    sns.barplot(x="species", y="petal length (cm)", data=df, ci=None)
    plt.title("Bar Chart: Average Petal Length per Species")
    plt.xlabel("Species")
    plt.ylabel("Average Petal Length (cm)")
    plt.show()

    # 3. Histogram
    plt.figure(figsize=(8, 5))
    plt.hist(df["sepal width (cm)"], bins=15, color="skyblue", edgecolor="black")
    plt.title("Histogram: Sepal Width Distribution")
    plt.xlabel("Sepal Width (cm)")
    plt.ylabel("Frequency")
    plt.show()

    # 4. Scatter Plot
    plt.figure(figsize=(8, 5))
    sns.scatterplot(
        x="sepal length (cm)",
        y="petal length (cm)",
        hue="species",
        data=df,
    )
    plt.title("Scatter Plot: Sepal Length vs Petal Length")
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Petal Length (cm)")
    plt.legend(title="Species")
    plt.show()

    
    # Error Handling Example
    
    try:
        df2 = pd.read_csv("non_existent_file.csv")
    except FileNotFoundError:
        print("\nError: File not found. Please check the file path.")


if __name__ == "__main__":
    main()
