import psycopg2
import logging
import os

from dotenv import load_dotenv
load_dotenv()

def get_connection():

    try:
        connection = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
        )

        logging.info(
            "Database connection establish"
        )

        return connection
    
    except Exception as e:

        logging.error(
            f"Database connection failed: {e}"
        )
        return None
    
conn = get_connection()


def load_to_postgres(clean_data):

    if clean_data is None:

        logging.warning(
            "No data received for loading"
        )

        return
    
    conn = None

    try:

        conn = get_connection()

        cursor = conn.cursor()

        insert_query = """
        INSERT INTO stock_prices
        (
            symbol,
            company_name,
            exchange,
            close_price,
            volume,
            trade_date
        )
        VALUES
        (
            %s,
            %s,
            %s,
            %s,
            %s,
            %s
        )

        ON CONFLICT (symbol, trade_date)
        DO NOTHING;
        """

        values = (
            clean_data["symbol"],
            clean_data["company_name"],
            clean_data["exchange"],
            clean_data["close_price"],
            clean_data["volume"],
            clean_data["trade_date"]
        )

        cursor.execute(
            insert_query,
            values
        )

        if cursor.rowcount == 0:

            logging.info(
            f"Duplicate record skipped for {clean_data['symbol']}"
            )

        else:

            logging.info(
            f"Inserted record for {clean_data['symbol']}"
            )

        conn.commit()

        logging.info(
            f"Loaded {clean_data['symbol']} into PostgreSQL"
        )

        print(
            f"{clean_data['symbol']} loaded successfully"
        )

    except Exception as e:

        logging.error(
            f"Load failed: {e}"
        )

        print(
            f"Load failed: {e}"
        )

    finally:
        if conn:
            conn.close()