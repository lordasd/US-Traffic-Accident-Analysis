import sqlite3
from questions import queries_with_questions

class SqliteExtractor:
    def __init__(self, duckdb_con, sqlite_db_path):
        self.duckdb_con = duckdb_con
        self.sqlite_db_path = sqlite_db_path

    # Extract specific queries into individual SQLite tables
    def extract_queries_to_sqlite(self):
        sqlite_con = sqlite3.connect(self.sqlite_db_path)

        # Save 50 rows to a new table
        fifty_rows_query = "SELECT * FROM accidents LIMIT 50"
        df_fifty_rows = self.duckdb_con.execute(fifty_rows_query).df()
        df_fifty_rows.to_sql('fifty_rows', sqlite_con, if_exists='replace', index=False)

        # Execute queries and save to SQLite tables
        for table_name, query_info in queries_with_questions.items():
            df = self.duckdb_con.execute(query_info['extraction_query']).df()
            df.to_sql(table_name, sqlite_con, if_exists='replace', index=False)

        # Close connections
        sqlite_con.close()