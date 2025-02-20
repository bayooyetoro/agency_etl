from utils import *


# set up logger
logger = setup_logger("my_logger", "main.log", filemode='w')


# file paths
json_file_path = "./data/raw_data.json"
csv_file_path = "./data/extracted_data.csv"
url = "https://restcountries.com/v3.1/all"


def main():
    try:
        logger.info("getting data from the API...")
        get_data(url, json_file_path)

        logger.info("File Saved Successfully! Starts Extraction...")
        extract_countries_data(json_file_path)

        logger.info("Extraction Completed! Transforming and loading to DB...")
        load_data_to_db(csv_file_path)
        
        logger.info("Data Loaded Successfully!")


    except Exception as e:
        logger.error(f"Error Occured: {e}")


if __name__ == "__main__":
    main()