import os
import requests
import zipfile

def extract_zip(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(".")

extract_zip("annual_aqi_by_cbsa_2024.zip")

AQI_URL = "https://aqs.epa.gov/aqsweb/airdata/annual_aqi_by_cbsa_2024.zip"
OUTPUT_FILE = "annual_aqi_by_cbsa_2024.zip"

def download_file(url, filename):
    print(f"Downloading {filename}...")

    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(filename, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    print(f"Saved: {filename}")

def main():
    download_file(AQI_URL, OUTPUT_FILE)

if __name__ == "__main__":
    main()
