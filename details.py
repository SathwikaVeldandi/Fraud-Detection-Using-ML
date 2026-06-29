import os
import pandas as pd

dataset_path = "dataset/creditcard.csv"

if not os.path.exists(dataset_path):
    print("Dataset not found!")
    print("Download it from:")
    print("https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud")
    print("Place creditcard.csv inside the dataset folder.")
else:
    df = pd.read_csv(dataset_path)

    print("Dataset Shape:", df.shape)
    print("\nColumns:")
    print(df.columns.tolist())
    print("\nFirst Five Rows:")
    print(df.head())