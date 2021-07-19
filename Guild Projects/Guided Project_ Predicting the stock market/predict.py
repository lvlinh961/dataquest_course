import pandas as pd
from datetime import datetime

df = pd.read_csv("sphist.csv")
df["Date"] = pd.to_datetime(df["Date"])
df.sort_values("Date", ascending=True, inplace=True)
print("-----")
print(df["Date"].head())

df["day_5"] = df["Close"].rolling(5).mean().shift(1)

print(df[df['Date'] == datetime(year=1951, month=1, day=3)])