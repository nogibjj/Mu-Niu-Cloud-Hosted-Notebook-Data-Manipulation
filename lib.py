import pandas as pd
import matplotlib.pyplot as plt


# Load the data
def load(path):
    df = pd.read_csv(path)
    return df


# Summary the data
def summary(path):
    data = load(path)
    num_columns = data.select_dtypes(include="number").columns
    data_summary = data[num_columns].describe()
    print(data_summary)
    return data_summary


# Visualize the data
def visualize(path):
    data = load(path)

    num_columns = data.select_dtypes(include="number").columns
    data[num_columns].hist(figsize=(12, 8), bins=15)
    plt.suptitle("Histograms of Numerical Features")
    plt.show()
