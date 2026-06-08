import logging

def transform_stock_data(raw_data):
    if raw_data is None:
        logging.error(
        "Transformation skipped because raw_data is None"
        )
        return None

    try:
        transformed_data = {
            "symbol":
                raw_data["symbol"],

            "company_name":
                raw_data["name"],

            "exchange":
                raw_data["exchange"],

            "close_price":
                float(raw_data["close"]),

            "volume":
                int(raw_data["volume"]),

            "trade_date":
                raw_data["datetime"]
        }

        logging.info(f"Transformation successful for {raw_data['symbol']}")
        return transformed_data

    except Exception as e:
        logging.error(f"Transformation failed: {e}")
        return None