import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("--input", required=True)
parser.add_argument("--out", required=True)
args = parser.parse_args()

df = pd.read_excel(args.input, skiprows=4)

df.columns = [
    "state", "city", "population", "violent_crime",
    "murder", "rape", "robbery", "aggravated_assault",
    "property_crime", "burglary", "larceny_theft",
    "motor_vehicle_theft", "arson"
]

df = df.dropna(subset=["city"])
df["state"] = df["state"].ffill()

numeric_cols = ["population", "violent_crime", "murder", "rape", "robbery",
                "aggravated_assault", "property_crime", "burglary",
                "larceny_theft", "motor_vehicle_theft", "arson"]
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")
df = df.dropna(subset=["population", "violent_crime"])
df = df.reset_index(drop=True)

print(f"Shape: {df.shape}")
print(df.describe())
print(df["violent_crime"].mean())
print(df["property_crime"].mean())

state_summary = df.groupby("state")[["violent_crime", "property_crime"]].sum()
print(state_summary.sort_values("violent_crime", ascending=False).head(10))

df.to_csv(args.out, index=False)
