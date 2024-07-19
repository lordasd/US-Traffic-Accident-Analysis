# Paths to the data and databases
DB_PATH = 'accidents.db'
CSV_PATH = 'US_Accidents_March23.csv'
DUCKDB_PATH = 'accidents.duckdb'
JSON_PATH = './fake_data.json'
NUM_RECORDS = 100000

# Plot types for different queries
plot_types = {
    "cities_with_most_accidents": "bar",
    "most_dangerous_streets": "barh",
    "quarterly_trend": "line",
    "accidents_by_hour": "pie",
    "common_weather_conditions": "seaborn_bar",
    "states_with_most_accidents": "seaborn_line",
    "top_10_cities_by_accidents": "barh"
}