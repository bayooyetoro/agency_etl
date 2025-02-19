import pandas as pd
import json
import requests
import logging


def setup_logger(name:str, log_file:str, filemode:str ='a', level=logging.INFO):
    """
        Function to setup logger with the specified name, log file, and logging level.
        
        :param name: Name of the logger.
        :param log_file: File to log messages.
        :param file_mode: mode of saving (default: append)
        :param level: Logging level (default: logging.INFO).
    """
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
                                  datefmt='%Y-%m-%d %H:%M:%S')
    
    logger = logging.getLogger(name)
    logger.setLevel(level)

    file_handler = logging.FileHandler(f"./logs/{log_file}")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


def get_data(url, file_name):
    """
    Fetches data from the API and save

    :param url: url link to API
    :param file_name: name to save the file in raw folder
    """
    response = requests.get(url)
    raw_data = response.json()

    with open(file_name, 'w') as file:
        json.dump(raw_data, file, indent=4)


def extract_countries_data(json_file_path):
    """
    Extracts specific columns from a JSON file containing country data.

    :param json_file_path: The path to the JSON file.

    Returns: A list of dictionaries, where each dictionary represents a country
             and contains the extracted data.  Returns an empty list if there's an error.
    """

    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    extracted_data = []

    for country in data:
        name = country.get("name", {})
        official_name = name.get("official")
        common_name = name.get("common")
        native_name = name.get("nativeName", {}).get("eng", {}).get("common")
        independence = country.get("independent")
        un_member = country.get("unMember")
        start_of_week = country.get("startOfWeek")
        currencies = country.get("currencies", {})
        currency_code = list(currencies.keys())[0] if currencies else None 
        currency_name = currencies.get(currency_code, {}).get("name") if currency_code else None
        currency_symbol = currencies.get(currency_code, {}).get("symbol") if currency_code else None
        idd_root = country.get("idd", {}).get("root", "")
        idd_suffixes = country.get("idd", {}).get("suffixes", [])
        country_code = idd_root + "".join(idd_suffixes)
        capital = country.get("capital")
        region = country.get("region")
        subregion = country.get("subregion")
        languages = country.get("languages", {})
        language_list = list(languages.values())
        area = country.get("area")
        population = country.get("population")
        continents = country.get("continents")

        extracted_data.append({
            "Country_Name": common_name,
            "Independence": independence,
            "UN_Member": un_member,
            "Start_of_Week": start_of_week,
            "Official_Country_Name": official_name,
            "Common_Native_Name": native_name,
            "Currency_Code": currency_code,
            "Currency_Name": currency_name,
            "Currency_Symbol": currency_symbol,
            "Country_Code": country_code,
            "Capital": capital,
            "Region": region,
            "Subregion": subregion,
            "Languages": language_list,
            "Area": area,
            "Population": population,
            "Continents": continents
        })

    with open("./data/extracted_countries.json", "w", encoding='utf-8') as outfile:
        json.dump(extracted_data, outfile, indent=4, ensure_ascii=False)

    df = pd.read_json("./data/extracted_countries.json", encoding='utf-8') 
    df.to_csv("./data/extracted_data.csv")






        

        