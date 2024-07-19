class DuckDBLoader:
    def __init__(self, csv_file_path, duckdb_con):
        self.csv_file_path = csv_file_path
        self.duckdb_con = duckdb_con

    def load_csv_to_duckdb(self):
        self.duckdb_con.execute(f"""
            CREATE TABLE IF NOT EXISTS accidents AS 
            SELECT * FROM read_csv_auto('{self.csv_file_path}');
        """)
