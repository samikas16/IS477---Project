rule all:
    input:
        "merged_aqi_crime.csv"

rule download:
    output:
        "annual_aqi_by_cbsa_2024.zip"
    shell:
        "python download_data.py"

rule verify_checksums:
    input:
        aqi="annual_aqi_by_cbsa_2024.csv",
        crime="crime_cleaned.csv"
    output:
        "checksums_verified.txt"
    shell:
        """
        python verify_checksums.py \
            --aqi {input.aqi} \
            --crime {input.crime} \
            && touch {output}
        """

rule merge:
    input:
        aqi="annual_aqi_by_cbsa_2024.csv",
        crime="crime_cleaned.csv"
    output:
        "merged_aqi_crime.csv"
    shell:
        "python merge.py --aqi {input.aqi} --crime {input.crime} --out {output}"

rule analyze:
    input:
        "merged_aqi_crime.csv"
    shell:
        "python analyze.py --merged {input}"
