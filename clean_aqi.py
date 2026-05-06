import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("--input", required=True)
parser.add_argument("--out", required=True)
args = parser.parse_args()

df = pd.read_csv(args.input)

print(f"Shape: {df.shape}")
print(df.dtypes)
print(df.isnull().sum())
print(df.describe())

df = df.dropna()
df = df.drop_duplicates()

print(df[["Good Days","Moderate Days","Unhealthy for Sensitive Groups Days",
          "Unhealthy Days","Very Unhealthy Days","Hazardous Days"]].mean())

print(df.groupby("CBSA")["Median AQI"].mean().sort_values(ascending=False).head())
print(df.groupby("CBSA")["Median AQI"].mean().sort_values(ascending=True).head())

df.to_csv(args.out, index=False)
