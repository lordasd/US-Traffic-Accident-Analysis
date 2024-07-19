# data_generator.py
from faker import Faker
from faker.providers import BaseProvider
import json
import os
import random

class DataGenerator:
    def __init__(self, num_records, output_path):
        self.num_records = num_records
        self.output_path = output_path
        self.fake = Faker()

    def generate_fake_data(self):
        data = []
        for _ in range(self.num_records):
            record = {
                "ID": self.fake.uuid4(),
                "Source": self.fake.word(),
                "Severity": self.fake.random_int(min=1, max=4),
                "Start_Time": self.fake.date_time_between(start_date='-5y', end_date='now').isoformat(),
                "End_Time": self.fake.date_time_between(start_date='-5y', end_date='now').isoformat(),
                "Start_Lat": float(self.fake.latitude()),
                "Start_Lng": float(self.fake.longitude()),
                "End_Lat": float(self.fake.latitude()),
                "End_Lng": float(self.fake.longitude()),
                "Distance(mi)": float(round(random.uniform(0.1, 10.0), 1)),
                "Description": self.fake.sentence(),
                "Street": self.fake.street_name(),
                "City": self.fake.city(),
                "State": self.fake.state_abbr(),
                "Zipcode": self.fake.zipcode(),
                "Country": self.fake.country(),
                "Timezone": self.fake.timezone(),
                "Airport_Code": self.fake.lexify(text='???'),
                "Weather_Timestamp": self.fake.date_time_between(start_date='-5y', end_date='now').isoformat(),
                "Temperature(F)": float(round(random.uniform(-30, 120), 1)),
                "Wind_Chill(F)": float(round(random.uniform(-30, 120), 1)),
                "Humidity(%)": self.fake.random_int(min=0, max=100),
                "Pressure(in)": float(round(random.uniform(29, 31), 2)),
                "Visibility(mi)": float(round(random.uniform(0, 10), 1)),
                "Wind_Direction": self.fake.random_element(elements=('N', 'S', 'E', 'W', 'NE', 'NW', 'SE', 'SW')),
                "Wind_Speed(mph)": float(round(random.uniform(0, 100), 1)),
                "Precipitation(in)": float(round(random.uniform(0, 2), 2)),
                "Weather_Condition": self.fake.random_element(elements=('Clear', 'Cloudy', 'Rain', 'Snow', 'Fog', 'Storm', 'Hail', 'Windy')),
                "Amenity": self.fake.boolean(),
                "Bump": self.fake.boolean(),
                "Crossing": self.fake.boolean(),
                "Give_Way": self.fake.boolean(),
                "Junction": self.fake.boolean(),
                "No_Exit": self.fake.boolean(),
                "Railway": self.fake.boolean(),
                "Roundabout": self.fake.boolean(),
                "Station": self.fake.boolean(),
                "Stop": self.fake.boolean(),
                "Traffic_Calming": self.fake.boolean(),
                "Traffic_Signal": self.fake.boolean(),
                "Turning_Loop": self.fake.boolean(),
                "Sunrise_Sunset": self.fake.random_element(elements=('Day', 'Night')),
                "Civil_Twilight": self.fake.random_element(elements=('Day', 'Night')),
                "Nautical_Twilight": self.fake.random_element(elements=('Day', 'Night')),
                "Astronomical_Twilight": self.fake.random_element(elements=('Day', 'Night'))
            }
            data.append(record)
        return data

    def save_data_to_file(self, data):
        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)
        with open(self.output_path, 'w') as f:
            json.dump(data, f, indent=4)

    def run(self):
        data = self.generate_fake_data()
        self.save_data_to_file(data)
        print(f"First 5 records generated: {data[:5]}")
        print(f"Fake data generated and saved to {self.output_path}")