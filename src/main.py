import time
import logging 

from logging_config import setup_logging

setup_logging()

from extract import fetch_stock_data
from transform import transform_stock_data
from load import load_to_postgres


symbols = [
    "IBM",
    "AAPL",
    "MSFT",
    "GOOGL",
    "AMZN",
    "TSLA"
]

for symbol in symbols:

    stock_data = fetch_stock_data(symbol)

    if stock_data is None:

        logging.warning(
            f"Skipping {symbol}"
        )

        continue

    clean_data = transform_stock_data(stock_data)

    if clean_data is None:

        logging.warning(
            f"Transformation failed for {symbol}"
        )

        continue

    load_to_postgres(clean_data)

    time.sleep(10)