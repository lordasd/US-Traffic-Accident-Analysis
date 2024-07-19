import streamlit as st

def dataset_story():
    st.title("US Accidents Dataset Story")
    
    st.subheader("Description")
    st.write("""
    This is a countrywide car accident dataset that covers 49 states of the USA. The accident data were collected from February 2016 to March 2023, using multiple APIs that provide streaming traffic incident (or event) data. These APIs broadcast traffic data captured by various entities, including the US and state departments of transportation, law enforcement agencies, traffic cameras, and traffic sensors within the road networks. The dataset currently contains approximately 7.7 million accident records.
    """)
    
    st.subheader("Content")
    st.write("""
    This dataset was collected in real-time using multiple Traffic APIs. It contains accident data collected from February 2016 to March 2023 for the Contiguous United States. For more details about this dataset, please visit [here](https://www.kaggle.com/sobhanmoosavi/us-accidents).
    """)
    
    st.subheader("Inspiration")
    st.write("""
    The US-Accidents dataset can be used for numerous applications, such as real-time car accident prediction, studying car accident hotspot locations, casualty analysis, extracting cause and effect rules to predict car accidents, and studying the impact of precipitation or other environmental stimuli on accident occurrence. The most recent release of the dataset can also be useful for studying the impact of COVID-19 on traffic behavior and accidents.
    """)
    
    st.subheader("Story Objective")
    st.write("""
    To provide a comprehensive picture of road accidents in the US, identify the locations, times, and main causes of accidents, and offer insights to improve road safety.
    """)

    st.subheader("How We Tell the Story")
    st.write("""
    1. **Cities with the Most Accidents:** We will present the top 10 cities with the highest number of accidents in recent years.
    2. **Most Dangerous Streets:** We will present the top 10 most dangerous streets based on the number of accidents.
    3. **Quarterly Trends:** We will present the quarterly trend of road accidents over the years.
    4. **Hours with the Most Accidents:** We will present the hours of the day during which most accidents occur.
    5. **Most Common Weather Conditions:** We will present the top 10 most common weather conditions during accidents.
    6. **States with the Most Accidents:** We will present the top 10 states with the highest number of accidents.
    """)

    st.subheader("Key Insights")
    st.write("""
    - Identifying dangerous cities and streets.
    - Understanding seasonal and peak hour patterns in accidents.
    - Identifying dangerous weather conditions for driving.
    - Focusing on states with a high number of accidents to improve infrastructure and road safety.
    """)

    st.subheader("Other Details")
    st.write("""
    Please note that the dataset may be missing data for certain days, which could be due to network connectivity issues during data collection. Regrettably, the dataset will no longer be updated, and this version should be considered the latest.
    """)
    
    st.subheader("Usage Policy and Legal Disclaimer")
    st.write("""
    This dataset is being distributed solely for research purposes under the Creative Commons Attribution-Noncommercial-ShareAlike license (CC BY-NC-SA 4.0). By downloading the dataset, you agree to use it only for non-commercial, research, or academic applications. If you use this dataset, it is necessary to cite the papers mentioned above.
    """)