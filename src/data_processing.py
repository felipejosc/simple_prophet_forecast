import pandas as pd

def load_and_clean(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.replace(' ', '_').str.lower()
    df['date'] = pd.to_datetime(df['date'], format='mixed')
    df = df.groupby('date')['money'].sum().reset_index()
    return df

def prepare_weekly(df: pd.DataFrame) -> pd.DataFrame:
    df = df.rename(columns={'date': 'ds', 'money': 'y'})
    df_weekly = df.resample('W-MON', on='ds').sum().reset_index()
    df_weekly['y_smooth'] = df_weekly['y'].rolling(3, center=True).mean()
    return df_weekly
