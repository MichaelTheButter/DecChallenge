# December Challenge: Weather Data Pipeline

![Project Logo](images/dec_logo.png)

## Overview

This project is part of the Big Data Academy, December Challenge. Involves building a data pipeline to fetch, process, and store weather data. The pipeline consists of several tasks, each focusing on different aspects of data handling, from fetching data from an API to loading it into a relational database. We used:
- pandas, 
- PySpark, 
- Structured Streaming
- AWS.

## Tasks

### Task 1: Fetch Weather Data

Write an application that fetches data from a weather API and saves it to disk/Cloud.

### Task 2: Process Data with Spark

Create a Spark job that reads JSON files, parses them into a usable state, and writes the combined data to a final Parquet file in another location. Use checkpoints and streaming to read only new data

### Task 3: Transform Data

Modify and transform the data to achieve its final shape, extracting meaningful information. 

### Task 4: Load Data into Relational Database

Load the transformed data into a relational database using Spark. 

## Project Structure

- `main.py`: The main entry point of the application.
- `extractor.py`: Contains classes for fetching and converting weather data.
- `file_writer.py`: Handles saving data to disk or cloud storage.
- `json_to_parquet.py`: Spark functions to transform JSON to Parquet files.
- `loader.py`: Spark functions for loading data into a relational database.
- `config/`: Configuration files for database credentials, schema definitions, and paths.

## How to Run

1. **Fetch Weather Data**:
   ```bash
   python main.py
   ```

2. **Run Spark Jobs**:
   If prompted, choose to run the Spark jobs to process and load the data.

## Requirements

- Python 3.x
- Apache Spark
- PySpark
- Pandas
- A weather API key
- Access to a relational database (e.g., SQL Server)
- AWS credentials for S3 storage (if using cloud storage)

## Configuration

Update the configuration files in the `config/` directory with your API keys, database credentials, and file paths.