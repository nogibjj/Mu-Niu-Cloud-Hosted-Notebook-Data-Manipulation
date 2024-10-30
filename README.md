[![Notebook Run](https://github.com/nogibjj/Mu-Niu-Cloud-Hosted-Notebook-Data-Manipulation/actions/workflows/CI.yml/badge.svg)](https://github.com/nogibjj/Mu-Niu-Cloud-Hosted-Notebook-Data-Manipulation/actions/workflows/CI.yml)

## Cloud Hosted Notebook Data Manipulation Project


## Project Overview

This project is designed for data manipulation and analysis using Google Colab notebooks hosted in a cloud environment. The primary focus is to streamline data processing tasks and generate insights through visualizations and summary statistics, with a CI pipeline implemented using GitHub Actions for automated testing and code quality checks.

## Features

- **Data Loading and Processing**: Load data from CSV files and perform basic data cleaning and manipulation.
- **Data Visualization**: Generate visualizations using `matplotlib` to gain insights into data trends.
- **Summary Statistics**: Calculate and display summary statistics for data analysis.
- **CI**: GitHub Actions workflows for automated testing and linting to maintain code quality.
- **Requirements Management**: `requirements.txt` for managing dependencies.

## Performance

1. Data Loading
   
```Python
df = pd.read_csv(path)
```

2. Data Summary

```Python
data = load(path)
# filter numerical columns
num_columns = data.select_dtypes(include="number").columns
data_summary = data[num_columns].describe()
```

3. Data Visualization

```Python
data = load(path)
# filter numerical columns
num_columns = data.select_dtypes(include="number").columns
data[num_columns].hist(figsize=(12, 8), bins=15)
plt.suptitle("Histograms of Numerical Features")
plt.show()
```


## Requirements

Dependencies are listed in the `requirements.txt` file for easy installation.


```Python
# install dependencies
make install

# format & code standard
make format
make lint

# test
make test
```

