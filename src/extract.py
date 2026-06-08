import requests
import logging
import os
import json

from dotenv import load_dotenv
load_dotenv()

def fetch_stock_data(symbol):
    """
    Extract stock data from Twelve Data API.

    Parameters:
        symbol (str): Stock ticker symbol
        api_key (str): Twelve Data API key

    Returns:
        dict | None
    """
    api_key = os.getenv("API_KEY")
    
    logging.info(f"Starting extraction for {symbol}")

    api_url = "https://api.twelvedata.com/quote"

    params = {
        "symbol": symbol,
        "apikey": api_key
    }

    try:
        response = requests.get(
            api_url,
            params=params,
            timeout=30
        )

        logging.info(
            f"HTTP Status Code for {symbol}: "
            f"{response.status_code}"
        )

        if response.status_code != 200:
            logging.error(
                f"Failed request for {symbol}. "
                f"Status Code: {response.status_code}"
            )

            return None

        data = response.json()

        logging.info(
            f"Raw API Response: {data}"
        )

        # Check if API returned an error
        if "code" in data:

            logging.error(
                f"API Error for {symbol}: {data}"
            )

            return None

        # Required business fields
        required_fields = [
            "symbol",
            "name",
            "exchange",
            "close",
            "volume",
            "datetime"
        ]

        # Validate fields
        for field in required_fields:

            if field not in data:

                logging.error(
                    f"Missing field '{field}' "
                    f"for {symbol}"
                )

                return None

        logging.info(
            f"Extraction successful for {symbol}"
        )

        return data

    except requests.exceptions.Timeout:

        logging.error(
            f"Timeout occurred while fetching {symbol}"
        )

        return None

    except requests.exceptions.RequestException as e:

        logging.error(
            f"Request failed for {symbol}: {e}"
        )

        return None

    except Exception as e:

        logging.error(
            f"Unexpected error for {symbol}: {e}"
        )

        return None
    



# Raw Data Layer
def save_raw_json(data, symbol):

    try:

        raw_folder = "data/raw"

        os.makedirs(
            raw_folder,
            exist_ok=True
        )

        file_path = os.path.join(
            raw_folder,
            f"{symbol}.json"
        )

        with open(
            file_path,
            "w"
        ) as json_file:

            json.dump(
                data,
                json_file,
                indent=4
            )

        logging.info(f"Raw JSON saved for {symbol}")

    except Exception as e:

        logging.error(
            f"Failed to save raw JSON for "
            f"{symbol}: {e}"
       )