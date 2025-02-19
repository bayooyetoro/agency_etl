from utils import *
import json

# setting up logger
logger = setup_logger("my_logger", "main.log", filemode='w')

url = "https://restcountries.com/v3.1/all"

# file paths
json_file_name = "./data/raw_data.json"
csv_file_path = "./data/extracted_data.csv"


def main():
    try:
        logger.info("getting data from the API...")
        get_data(url, json_file_name)

        logger.info("File Saved Successfully! Starts Extraction...")
        extract_countries_data(json_file_name)

        logger.info("Extraction Completed! Transforming and loading to DB...")



    except Exception as e:
        logger.error(f"Error Occured:{e}")


if __name__ == "__main__":
    main()