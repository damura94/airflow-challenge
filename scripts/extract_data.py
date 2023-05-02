import pandas as pd

def extract():
    df = pd.read_csv('../data/Traffic_Flow_Map_Volumes.csv')
    return df
