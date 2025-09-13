# Iris Dataset Analysis and Visualization

This project performs an exploratory data analysis (EDA) on the famous Iris flower dataset using Python and popular data science libraries.

## Overview

The script loads the Iris dataset, performs basic data analysis, and creates several visualizations to understand the characteristics of different Iris species (Setosa, Versicolor, and Virginica).

## Features

- **Data Loading**: Loads the Iris dataset from scikit-learn
- **Data Exploration**: Provides basic information about the dataset
- **Data Cleaning**: Handles missing values (though the Iris dataset typically has none)
- **Statistical Analysis**: Calculates descriptive statistics and group means
- **Data Visualization**: Creates multiple plots to visualize relationships between features

## Visualizations Included

1. **Line Chart**: Sepal length across samples
2. **Bar Chart**: Average petal length per species
3. **Histogram**: Distribution of sepal width
4. **Scatter Plot**: Sepal length vs. petal length colored by species

## Requirements

- Python 3.x
- pandas
- matplotlib
- seaborn
- scikit-learn

## Installation

1. Clone or download this repository
2. Install the required packages:

```bash
pip install pandas matplotlib seaborn scikit-learn
```

## Usage

Run the script directly:

```bash
python data_analysis_assignment.py
```

## Output

The script will:
1. Print dataset information, including first few rows, data types, and missing values
2. Display basic statistics and mean values per species
3. Show key observations about the data
4. Generate and display four different visualizations
5. Demonstrate error handling for file operations

## Key Observations

- Setosa flowers generally have smaller petal lengths and widths
- Virginica species tend to have the largest petal measurements
- Sepal length shows less variation across species compared to petal length

## Error Handling

The script includes a simple error handling example for file operations, demonstrating how to catch and handle `FileNotFoundError` exceptions.
