import hashlib
import argparse
<<<<<<< HEAD
import sys
=======
>>>>>>> 895b4985f68bd114f51d1c55050184322c12f7ae

EXPECTED_HASHES = {
    "annual_aqi_by_cbsa_2024.csv": "548c45b5b8822f5bcd988a17ea55726134ca668b82151c418ce3f7b3b2663cff",
    "crime_cleaned.csv": "9ede2384558c90fe0a5b22d68ae41d2449755d0d6de7dad64681ea0d297dd0b8"
}

def compute_sha256(file_path):
    sha256 = hashlib.sha256()
<<<<<<< HEAD
    with open(file_path, "rb") as f:
        for block in iter(lambda: f.read(4096), b""):
            sha256.update(block)
=======

    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)

>>>>>>> 895b4985f68bd114f51d1c55050184322c12f7ae
    return sha256.hexdigest()

def verify(file_path):
    filename = file_path.split("/")[-1]
<<<<<<< HEAD
    actual_hash = compute_sha256(file_path)
    expected_hash = EXPECTED_HASHES.get(filename)

    print(f"\nChecking {filename}")
=======

    actual_hash = compute_sha256(file_path)
    expected_hash = EXPECTED_HASHES.get(filename)

    print(f"{filename}")
>>>>>>> 895b4985f68bd114f51d1c55050184322c12f7ae
    print(f"Actual:   {actual_hash}")
    print(f"Expected: {expected_hash}")

    if actual_hash != expected_hash:
<<<<<<< HEAD
        print(f"❌ Checksum FAILED for {filename}")
        sys.exit(1)
    else:
        print(f"✅ Checksum PASSED for {filename}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--aqi", required=True)
    parser.add_argument("--crime", required=True)
=======
        raise ValueError(f"Checksum FAILED for {filename}")

    print(f"Checksum PASSED for {filename}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--aqi")
    parser.add_argument("--crime")
>>>>>>> 895b4985f68bd114f51d1c55050184322c12f7ae
    args = parser.parse_args()

    verify(args.aqi)
    verify(args.crime)

<<<<<<< HEAD
    # REQUIRED for Snakemake (output file)
    with open("checksums_verified.txt", "w") as f:
        f.write("All checksums passed.\n")

if __name__ == "__main__":
    main()
=======
if __name__ == "__main__":
    main()
>>>>>>> 895b4985f68bd114f51d1c55050184322c12f7ae
