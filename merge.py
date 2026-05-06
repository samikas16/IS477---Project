import pandas as pd
import argparse

def main(aqi_path, crime_path, out_path):
    aqi_df = pd.read_csv(aqi_path)
    crime_df = pd.read_csv(crime_path)

    aqi_df["city"] = (
        aqi_df["CBSA"]
        .str.split(",").str[0]
        .str.split("-").str[0]
        .str.strip()
        .str.lower()
    )
    crime_df["city"] = crime_df["city"].str.strip().str.lower()

    aqi_df = aqi_df.drop_duplicates(subset=["city"])
    crime_df = crime_df.drop_duplicates(subset=["city"])

    crime_agg = crime_df.groupby("city").agg({
        "population": "sum",
        "violent_crime": "sum",
        "property_crime": "sum",
        "murder": "sum",
        "rape": "sum",
        "robbery": "sum",
        "aggravated_assault": "sum",
        "burglary": "sum",
        "larceny_theft": "sum",
        "motor_vehicle_theft": "sum",
        "arson": "sum"
    }).reset_index()

    merged = pd.merge(aqi_df, crime_agg, on="city", how="inner")
    merged = merged[merged["population"] > 0].copy()
    merged["violent_crime_rate"] = (merged["violent_crime"] / merged["population"]) * 100_000
    merged["property_crime_rate"] = (merged["property_crime"] / merged["population"]) * 100_000

    print("Merged dataset shape:", merged.shape)
    merged.to_csv(out_path, index=False)
    print(f"Merged dataset saved to {out_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--aqi", required=True)
    parser.add_argument("--crime", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    main(args.aqi, args.crime, args.out)