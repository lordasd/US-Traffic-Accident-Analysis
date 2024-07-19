import duckdb
from duckdb_loader import DuckDBLoader
from sqlite_extractor import SqliteExtractor
from data_generator import DataGenerator
from spark_processor import SparkProcessor
import config

def main():
    # Connect to DuckDB
    duckdb_con = duckdb.connect(config.DUCKDB_PATH)

    # Load data into DuckDB using DuckDBLoader
    loader = DuckDBLoader(config.CSV_PATH, duckdb_con)
    loader.load_csv_to_duckdb()
    print("Data loaded into DuckDB.")

    # Extract specific queries into individual SQLite tables
    extractor = SqliteExtractor(duckdb_con, config.DB_PATH)
    extractor.extract_queries_to_sqlite()
    print("Data extracted to SQLite tables.")

    # Close DuckDB connection
    duckdb_con.close()

    # Generate fake data
    generator = DataGenerator(num_records=config.NUM_RECORDS, output_path=config.JSON_PATH)
    generator.run()
    
    # Process large data using Spark
    processor = SparkProcessor(json_file_path=config.JSON_PATH)
    processor.process_data()
    print("Spark processing completed and data saved to small_data.db.")

if __name__ == "__main__":
    main()
