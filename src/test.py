import json

def extract_country_data(json_file_path):
    """
    Extracts specific columns from a JSON file containing country data.

    Args:
        json_file_path: The path to the JSON file.

    Returns:
        A list of dictionaries, where each dictionary represents a country
        and contains the extracted data.  Returns an empty list if there's an error.
    """

    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File not found at {json_file_path}")
        return []
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {json_file_path}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


    extracted_data = []

    for country in data:
        try: 
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
        except Exception as e:
            print(f"Error processing a country: {e}") 
    return extracted_data


file_path = "./data/raw_data.json"
extracted_data = extract_country_data(file_path)

if extracted_data:
    with open("./data/extracted_countries.json", "w", encoding='utf-8') as outfile:
        json.dump(extracted_data, outfile, indent=4, ensure_ascii=False)