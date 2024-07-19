from pyspark.sql import SparkSession
from pyspark.sql.functions import year, col
import sqlite3
from config import DB_PATH

class SparkProcessor:
    def __init__(self, json_file_path):
        self.json_file_path = json_file_path
        self.spark = SparkSession.builder.appName("Accident Data Processor").getOrCreate()
        self.df = self.spark.read.option("multiline", "true").json(self.json_file_path)
    
    def process_data(self):
        # Print the schema of the DataFrame
        self.df.printSchema()
        
        # Show a sample of the data to inspect
        self.df.show(5, truncate=False)
        
        # Process the data as intended
        filtered_df = self.df.filter(year(col("Start_Time")).between(2019, 2023))
        filtered_df.createOrReplaceTempView("accidents")
        
        query = """
        SELECT City, COUNT(*) as Accidents_Count
        FROM accidents
        GROUP BY City
        ORDER BY Accidents_Count DESC
        LIMIT 10
        """
        result_df = self.spark.sql(query)
        result_df.show()

        pandas_df = result_df.toPandas()
        conn = sqlite3.connect(DB_PATH)
        pandas_df.to_sql('top_10_cities_by_accidents', conn, if_exists='replace', index=False)
        conn.close()
