import os
import requests
<<<<<<< HEAD
=======
import zipfile

def extract_zip(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(".")

extract_zip("annual_aqi_by_cbsa_2024.zip")
>>>>>>> 895b4985f68bd114f51d1c55050184322c12f7ae

AQI_URL = "https://aqs.epa.gov/aqsweb/airdata/annual_aqi_by_cbsa_2024.zip"
OUTPUT_FILE = "annual_aqi_by_cbsa_2024.zip"

def download_file(url, filename):
<<<<<<< HEAD
    print(f"Downloading {filename}...")
=======
>>>>>>> 895b4985f68bd114f51d1c55050184322c12f7ae

    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(filename, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

<<<<<<< HEAD
    print(f"Saved: {filename}")

=======
>>>>>>> 895b4985f68bd114f51d1c55050184322c12f7ae
def main():
    download_file(AQI_URL, OUTPUT_FILE)

if __name__ == "__main__":
<<<<<<< HEAD
    main()
=======
    main()
>>>>>>> 895b4985f68bd114f51d1c55050184322c12f7ae
