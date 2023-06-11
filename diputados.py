from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def read_csv(filename):
    data = pd.read_csv(filename, error_bad_lines=False, skip_blank_lines=True)
    return data

# Example usage
filename = 'diputados.csv'  # Replace with the path to your CSV file
csv_data = read_csv(filename)

# Accessing the data
print(csv_data.head())  # Print the first few rows of the data
print(csv_data.info()) 
print(csv_data['ID_CASILLA'].value_counts())
print(csv_data.describe())

#This code help to 
IMAGES_PATH = Path() / "images" / "end_to_end_project"
IMAGES_PATH.mkdir(parents=True, exist_ok=True)

def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=300):
    path = IMAGES_PATH / f"{fig_id}.{fig_extension}"
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)

plt.rc('font', size=14)
plt.rc('axes', labelsize=14, titlesize=14)
plt.rc('legend', fontsize=14)
plt.rc('xtick', labelsize=10, color='#DE0058')
plt.rc('ytick', labelsize=10, color='#DE0058')


csv_data.hist(bins=50, figsize=(12, 8), color='purple')
save_fig("attribute_histogram_plots")
plt.show()

def shuffle_and_split_data(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]

train_set, test_set = shuffle_and_split_data(csv_data, 0.2)
len(train_set)
len(test_set)