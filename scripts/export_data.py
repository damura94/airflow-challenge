import pandas as pd

def export(df):
    df.to_csv('../data/data_transformed.csv', index=False)
