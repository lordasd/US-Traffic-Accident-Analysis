# US Accidents Analysis Project

## Project Description
This project analyzes a comprehensive dataset of US traffic accidents. It uses various data processing techniques, including DuckDB for initial data loading, SQLite for storage, and Apache Spark for big data processing. The project aims to derive insights about accident patterns, dangerous locations, and other relevant factors contributing to traffic accidents in the US.

## Dataset
The project uses the "US Accidents (March 2023)" dataset, which contains traffic accident records covering 49 states of the United States. The dataset is available on Kaggle: [US Accidents (March 2023)](https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents)

## Submitters
- **David Zaydenberg**, Davidzay@edu.hac.ac.il
- **Ron Elian**, Ronel@edu.hac.ac.il

## Prerequisites
- Python 3.8+
- Libraries: pandas, duckdb, sqlite3, pyspark, streamlit, matplotlib, seaborn, faker
- Sufficient storage space for the dataset and processed data

## List of Submitted Files (within the ZIP file)

1. **app.py**: Main script for data processing pipeline.
2. **duckdb_loader.py**: Loads data into DuckDB.
3. **sqlite_extractor.py**: Extracts data from DuckDB to SQLite.
4. **story.py**: Presents the dataset story using Streamlit.
5. **questions.py**: Contains queries for data analysis.
6. **data_generator.py**: Generates fake accident data.
7. **spark_processor.py**: Processes fake data using PySpark.
8. **visualizer.py**: Creates interactive dashboard with Streamlit.
9. **config.py**: Configuration file for the project.
10. **requirements.txt**: List of required Python packages.

## Instructions to Run

1. Install required packages:
pip install -r requirements.txt

2. Run the main processing script:
python app.py

3. Launch the Streamlit dashboard:
streamlit run visualizer.py

4. Open your web browser and navigate to the local address provided by Streamlit (usually http://localhost:8501).

## Known Limitations
- The fake data generation process may not perfectly represent real-world accident patterns.
- Processing large datasets may require significant computational resources.

## Contributing
If you'd like to contribute to this project or report any issues, please open an issue or submit a pull request on the project's repository.

## License
This project is licensed under the MIT License - see the `LICENSE` file for details.
