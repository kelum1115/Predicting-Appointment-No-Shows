import pandas as pd
import numpy as np

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    # Add a patient ID
    df = df.copy()
    df['PatientId'] = range(1, df.shape[0] + 1)
    df = df.set_index('PatientId')

    # Rename columns
    df = df.rename(columns={
        'Neighbourhood': 'Neighborhood',
        'Scholarship': 'SocialWelfare',
        'Hipertension': 'Hypertension',
        'Handcap': 'Handicap'
    })

    # Map target
    df['No-show'] = df['No-show'].map({'No': 0, 'Yes': 1}).astype(int)

    # Replace common invalid entries with NA
    df = df.replace(["", " ", "?", ".."], pd.NA)

    # Convert dates
    for col in ['ScheduledDay', 'AppointmentDay']:
        df[col] = pd.to_datetime(df[col]).dt.tz_localize(None)

    # Calculate DaysWaited
    df['DaysWaited'] = (
        df['AppointmentDay'].dt.normalize()
        - df['ScheduledDay'].dt.normalize()
    ).dt.days

    # Fix negative DaysWaited
    df['DaysWaited'] = df['DaysWaited'].replace([-1, -6], 4)

    # Fix invalid ages
    df.loc[(df['Age'] > 103) | (df['Age'] < 0), 'Age'] = np.nan
    df['Age'] = df['Age'].fillna(df['Age'].median()).astype(int)

    # Convert Handicap to boolean
    df['Handicapped'] = df['Handicap'] > 0

    return df


if __name__ == "__main__":
    print("loading data...")

    df = pd.read_csv("data/KaggleV2-May-2016.csv")  # load dataset first
    df = clean_data(df)  # then clean it

    print(df.head())