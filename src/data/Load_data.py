import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

if __name__ == "__main__":
    print("loading data...")
    
    df = load_data("data/KaggleV2-May-2016.csv")
    print(df.head())
