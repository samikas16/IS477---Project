rule all:
    input:
        "merged_aqi_crime.csv",
        "checksums_verified.txt",
        "analysis_output.txt"

rule download_aqi:
    output:
        "annual_aqi_by_cbsa_2024.zip"
    shell:
        "python3 download_data.py"

rule extract_aqi:
    input:
        "annual_aqi_by_cbsa_2024.zip"
    output:
        "annual_aqi_by_cbsa_2024.csv"
    shell:
        """
        python3 -c "
import zipfile;
with zipfile.ZipFile('{input}', 'r') as z:
    z.extractall('.')
        "
        """

rule clean_aqi:
    input:
        "annual_aqi_by_cbsa_2024.csv"
    output:
        "annual_aqi_by_cbsa_2024_clean.csv"
    shell:
        "python3 clean_aqi.py --input {input} --out {output}"

rule clean_crime:
    input:
        "CIUS_Table_8_Offenses_Known_to_Law_Enforcement_by_State_by_City_2024.xlsx"
    output:
        "crime_cleaned.csv"
    shell:
        "python3 clean_crime.py --input {input} --out {output}"

rule verify:
    input:
        aqi="annual_aqi_by_cbsa_2024.csv",
        crime="crime_cleaned.csv"
    output:
        "checksums_verified.txt"
    shell:
        "python3 verify_checksums.py --aqi {input.aqi} --crime {input.crime}"

rule merge:
    input:
        aqi="annual_aqi_by_cbsa_2024.csv",
        crime="crime_cleaned.csv"
    output:
        "merged_aqi_crime.csv"
    shell:
        "python3 merge.py --aqi {input.aqi} --crime {input.crime} --out {output}"

rule analyze:
    input:
        "merged_aqi_crime.csv"
    output:
        "analysis_output.txt",
        "plot1_aqi_violent.png",
        "plot2_aqi_property.png",
        "plot3_quartiles.png",
        "plot4_boxplot.png"
    shell:
        "python3 analyze.py --merged {input}"