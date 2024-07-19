queries_with_questions = {
    "cities_with_most_accidents": {
        "question": "Which 10 cities in the US reported the most accidents in the last 5 years?",
        "extraction_query": """
            SELECT City, Start_Time, Severity, cnt
            FROM (
                SELECT City, 
                    Start_Time, 
                    Severity, 
                    COUNT(*) OVER (PARTITION BY City) as cnt, 
                    ROW_NUMBER() OVER (PARTITION BY City ORDER BY Start_Time) as rn
                FROM accidents 
                WHERE strftime('%Y', Start_Time) BETWEEN '2018' AND '2023'
            ) sub
            WHERE rn = 1
            ORDER BY cnt DESC
            LIMIT 10;

        """
    },
    "most_dangerous_streets": {
        "question": "What are the 10 most dangerous streets based on the number of accidents?",
        "extraction_query": """
            SELECT Street, City, State, Severity, cnt
            FROM (
                SELECT Street, 
                    City, 
                    State, 
                    Severity, 
                    COUNT(*) OVER (PARTITION BY Street, City, State, Severity) as cnt, 
                    ROW_NUMBER() OVER (PARTITION BY Street, City, State, Severity ORDER BY Street) as rn
                FROM accidents 
            ) sub
            WHERE rn = 1
            ORDER BY cnt DESC
            LIMIT 10;
        """
    },
    "quarterly_trend": {
        "question": "What is the quarterly trend of accidents in the US?",
        "extraction_query": """
            SELECT year, month, count
            FROM (
                SELECT strftime('%Y', Start_Time) as year, 
                    strftime('%m', Start_Time) as month, 
                    COUNT(*) OVER (PARTITION BY strftime('%Y', Start_Time), strftime('%m', Start_Time)) as count, 
                    ROW_NUMBER() OVER (PARTITION BY strftime('%Y', Start_Time), strftime('%m', Start_Time) ORDER BY Start_Time) as rn
                FROM accidents
            ) sub
            WHERE rn = 1
            ORDER BY year, month;
        """
    },
    "accidents_by_hour": {
        "question": "During which hours of the day do most accidents occur?",
        "extraction_query": """
            SELECT strftime('%H', Start_Time) as hour, COUNT(*) as count 
            FROM accidents 
            GROUP BY hour 
            HAVING COUNT(*) > 0
            ORDER BY hour ASC;
        """
    },
    "common_weather_conditions": {
        "question": "What are the 10 most common weather conditions during accidents?",
        "extraction_query": """
            SELECT Weather_Condition, strftime('%H', ANY_VALUE(Start_Time)) as hour, COUNT(*) as count 
            FROM accidents 
            WHERE Weather_Condition IS NOT NULL
            GROUP BY Weather_Condition 
            ORDER BY count DESC 
            LIMIT 10;
        """
    },
    "states_with_most_accidents": {
        "question": "Which 10 states in the US report the most accidents?",
        "extraction_query": """
            SELECT State, COUNT(*) as count 
            FROM accidents 
            GROUP BY State 
            HAVING COUNT(*) > 0
            ORDER BY count DESC 
            LIMIT 10;
        """
    }
}
