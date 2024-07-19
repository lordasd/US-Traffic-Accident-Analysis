import sqlite3
from typing import List, Dict, Any
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from questions import queries_with_questions
from story import dataset_story

# Configuration
from config import plot_types, DB_PATH

# Database operations
class DatabaseManager:
    @staticmethod
    @st.cache_data
    def execute_query(query: str) -> pd.DataFrame:
        with sqlite3.connect(DB_PATH) as conn:
            return pd.read_sql_query(query, conn)

    @staticmethod
    def get_date_range(table_name: str) -> tuple:
        query = f"SELECT MIN(Start_Time) as min_date, MAX(Start_Time) as max_date FROM {table_name}"
        df = DatabaseManager.execute_query(query)
        return df['min_date'][0], df['max_date'][0]

    @staticmethod
    def get_unique_column_values(table_name: str, column_name: str) -> List[str]:
        query = f"SELECT DISTINCT {column_name} FROM {table_name}"
        df = DatabaseManager.execute_query(query)
        return df[column_name].tolist()

# Visualization functions
class Visualizer:
    @staticmethod
    def create_plot(df: pd.DataFrame, plot_type: str, x_col: str, y_col: str, title: str):
        plt.figure(figsize=(15, 8))
        if plot_type == 'bar':
            plt.bar(df[x_col].astype(str), df[y_col])
        elif plot_type == 'barh':
            plt.barh(df[x_col], df[y_col])
        elif plot_type == 'line':
            plt.plot(df[x_col], df[y_col])
        elif plot_type == 'pie':
            plt.pie(df[y_col], labels=df[x_col], autopct='%1.1f%%')
        elif plot_type == 'seaborn_bar':
            sns.barplot(data=df, x=x_col, y=y_col)
        elif plot_type == 'seaborn_line':
            sns.lineplot(data=df, x=x_col, y=y_col)
        plt.title(title)
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        st.pyplot(plt)

# Main application
class AccidentDataApp:
    def __init__(self):
        self.db_manager = DatabaseManager()

    def run(self):
        st.title("Accident Data Visualizations")
        sidebar_option = st.sidebar.selectbox("Choose an option", ["Story", "Questions", "Visualization", "Spark Visualization"])

        if sidebar_option == "Story":
            self.show_story()
        elif sidebar_option == "Questions":
            self.show_questions()
        elif sidebar_option == "Visualization":
            self.show_visualization()
        elif sidebar_option == "Spark Visualization":
            self.show_spark_visualization()

    def show_story(self):
        dataset_story()
        df_fifty_rows = self.db_manager.execute_query("SELECT * FROM fifty_rows")
        st.subheader("Sample Data (50 Rows)")
        st.dataframe(df_fifty_rows)

    def show_questions(self):
        st.write("### Questions")
        for _, value in queries_with_questions.items():
            st.write(f"**{value['question']}**")

    def show_visualization(self):
        query_name = st.selectbox("Select Query", list(queries_with_questions.keys()))
        additional_filter = self.get_additional_filters(query_name)
        self.visualize_table(query_name, queries_with_questions[query_name], additional_filter)

    def get_additional_filters(self, query_name: str) -> str:
        if query_name == "most_dangerous_streets":
            states = self.db_manager.get_unique_column_values(query_name, 'State')
            selected_states = st.multiselect("Select States", states)
            return f"State IN ({', '.join([f'\'{state}\'' for state in selected_states])})" if selected_states else "1=1"
        elif query_name == "common_weather_conditions":
            start_hour, end_hour = st.slider("Select Time of Day Range", 0, 23, (0, 23))
            return f"hour BETWEEN '{start_hour:02d}' AND '{end_hour:02d}'"
        return None

    def visualize_table(self, table_name: str, query_info: Dict[str, Any], additional_filter: str = None):
        query = f"SELECT * FROM {table_name}"
        if additional_filter:
            query += f" WHERE {additional_filter}"
        
        df = self.db_manager.execute_query(query)

        if df.isnull().values.any():
            st.write("Data contains null values. Please check the data source.")
            return

        if df.shape[1] < 2:
            st.write("Data frame does not have enough columns for plotting.")
            return

        st.write(f"#### Description of {query_info['question']}")
        
        plot_type = plot_types[table_name]
        x_col, y_col = df.columns[0], df.columns[-1]
        Visualizer.create_plot(df, plot_type, x_col, y_col, query_info['question'])

        st.write(f"### Data for {query_info['question']}")
        st.dataframe(df)

    def show_spark_visualization(self):
        st.write("### Spark Data Visualization")
        try:
            df = self.db_manager.execute_query("SELECT * FROM top_10_cities_by_accidents")
            Visualizer.create_plot(df, 'barh', 'City', 'Accidents_Count', 'Top 10 Cities with the Highest Number of Accidents')
            st.write("### Accident Counts by City")
            st.dataframe(df)
        except Exception as e:
            st.error("Unable to load Spark data. The 'top_10_cities_by_accidents' table does not exist in the database.")
            st.write("This could be because:")
            st.write("1. The Spark job hasn't been run yet.")
            st.write("2. The Spark job didn't complete successfully.")
            st.write("3. The results weren't properly saved to the SQLite database.")
            st.write("Please ensure that the Spark data processing step has been completed successfully before viewing this visualization.")

if __name__ == "__main__":
    app = AccidentDataApp()
    app.run()