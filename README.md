# Financial ETL Pipeline using Python, PostgreSQL, and Windows Task Scheduler

## Project Overview

This project is an end-to-end ETL (Extract, Transform, Load) pipeline that automatically collects stock market data from the Twelve Data API, transforms the raw data into a clean format, and stores it in a PostgreSQL database.

The pipeline is fully automated using Windows Task Scheduler and includes production-grade features such as logging, error handling, duplicate prevention, and environment variable management.

---

## Project Objectives

The primary objectives of this project are:

* Extract stock market data from an external REST API
* Transform raw API responses into a structured format
* Load cleaned data into PostgreSQL
* Prevent duplicate data insertion
* Automate daily execution
* Implement proper logging and monitoring
* Follow ETL best practices used in real-world Data Engineering projects

---

## Tech Stack

### Programming Language

* Python

### Database

* PostgreSQL

### API Source

* Twelve Data API

### Libraries Used

* requests
* psycopg2-binary
* python-dotenv
* logging
* json
* os
* time

### Automation

* Windows Task Scheduler

---

## Project Structure

financial_etl_project/

├── data/

│   └── raw_json_files/

├── logs/

│   └── pipeline.log

├── src/

│   ├── main.py

│   ├── extract.py

│   ├── transform.py

│   ├── load.py

│   ├── config.py

│   ├── logging_config.py

│   └── .env

├── run_etl.bat

└── README.md

---

## ETL Workflow

### Step 1: Extract

The extract module connects to the Twelve Data API and fetches stock market information for selected companies.

Stocks used:

* IBM
* AAPL
* MSFT
* GOOGL
* AMZN
* TSLA

Data extracted:

* Symbol
* Company Name
* Exchange
* Open Price
* High Price
* Low Price
* Close Price
* Volume
* Trade Date

Raw API responses are stored as JSON files for auditing and debugging purposes.

---

### Step 2: Transform

The transform module cleans and standardizes the extracted data.

Transformations performed:

* Rename fields
* Convert close price to float
* Convert volume to integer
* Remove unnecessary API fields
* Create a clean structured dictionary

Example:

Raw API:

{
"symbol": "AAPL",
"name": "Apple Inc.",
"close": "307.34000",
"volume": "65246700"
}

Transformed Data:

{
"symbol": "AAPL",
"company_name": "Apple Inc.",
"close_price": 307.34,
"volume": 65246700
}

---

### Step 3: Load

The load module inserts transformed records into PostgreSQL.

Table:

stock_prices

Columns:

* id
* symbol
* company_name
* exchange
* close_price
* volume
* trade_date
* created_at

---

## Database Schema

CREATE TABLE stock_prices (
id SERIAL PRIMARY KEY,
symbol VARCHAR(10),
company_name VARCHAR(200),
exchange VARCHAR(50),
close_price NUMERIC(12,2),
volume BIGINT,
trade_date DATE,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

---

## Duplicate Prevention

To prevent duplicate data insertion, a composite unique constraint was added.

ALTER TABLE stock_prices
ADD CONSTRAINT unique_stock_date
UNIQUE(symbol, trade_date);

The load query uses:

INSERT INTO stock_prices (...)
VALUES (...)
ON CONFLICT (symbol, trade_date)
DO NOTHING;

Benefits:

* Prevents duplicate records
* Allows safe reruns of ETL
* Supports idempotent data loading

---

## Logging Implementation

A centralized logging system was implemented.

Log file:

logs/pipeline.log

Logged Events:

* Extraction start
* API response status
* Transformation success/failure
* Database connection status
* Data load status
* Duplicate record detection
* Error messages

Example Log:

2026-06-08 09:00:05 - INFO - Extraction successful for IBM

2026-06-08 09:00:05 - INFO - Transformation successful for IBM

2026-06-08 09:00:05 - INFO - Loaded IBM into PostgreSQL

---

## Error Handling

Implemented error handling for:

### API Failures

* Invalid API key
* Network issues
* HTTP errors

### Transformation Errors

* Missing fields
* Invalid data types

### Database Errors

* Connection failures
* Insert failures
* Constraint violations

---

## Environment Variables

Sensitive information is stored in a .env file.

Example:

API_KEY=your_api_key

DB_HOST=localhost

DB_NAME=financial_etl

DB_USER=postgres

DB_PASSWORD=your_password

DB_PORT=5432

Benefits:

* Improved security
* No hardcoded credentials
* Easier deployment

---

## Automation Using Windows Task Scheduler

The pipeline is automated using Windows Task Scheduler.

Execution Flow:

Task Scheduler

↓

run_etl.bat

↓

main.py

↓

Extract

↓

Transform

↓

Load

↓

PostgreSQL

The scheduler runs automatically at a predefined time each day.

---

## Batch File

run_etl.bat

@echo off

cd /d C:\Users\HARSHVARDHAN\OneDrive\Desktop\financial_etl_project\src

python main.py

This batch file is triggered by Windows Task Scheduler.

---

## Sample Output

Database Records:

| Symbol | Company Name                                | Exchange | Close Price | Trade Date |
| ------ | ------------------------------------------- | -------- | ----------- | ---------- |
| IBM    | International Business Machines Corporation | NYSE     | 284.84      | 2026-06-05 |
| AAPL   | Apple Inc.                                  | NASDAQ   | 307.34      | 2026-06-05 |
| MSFT   | Microsoft Corp.                             | NASDAQ   | 416.67      | 2026-06-05 |

---

## Key Features

* REST API Integration
* ETL Architecture
* PostgreSQL Storage
* JSON Data Archiving
* Centralized Logging
* Error Handling
* Duplicate Prevention
* Environment Variable Management
* Automated Scheduling
* Production-style Project Structure

---

## Skills Demonstrated

### Data Engineering

* ETL Development
* Data Ingestion
* Data Transformation
* Database Loading
* Data Validation

### Python

* Functions
* Modules
* Exception Handling
* Logging
* File Handling
* API Integration

### SQL

* Table Creation
* Constraints
* Inserts
* Unique Keys
* PostgreSQL Operations

### Automation

* Windows Task Scheduler
* Batch Scripting

---

## Future Improvements

* Historical Stock Data Backfill
* Incremental Loading
* Docker Containerization
* Airflow Orchestration
* AWS Deployment
* Data Warehouse Integration
* Monitoring Dashboard
* Automated Email Alerts

---

## Author

Harshvardhan Patil

Financial ETL Pipeline Project

Python | SQL | PostgreSQL | Data Engineering
