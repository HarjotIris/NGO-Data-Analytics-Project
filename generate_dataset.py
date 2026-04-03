import pandas as pd
import numpy as np
import random

random.seed(42) #now whenever u call random functions, u get same random numbers

months = pd.date_range(start="2023-01-01", periods=36, freq="MS")
programs = ["literacy", "vocational", "digital skills"]
cities = ["Delhi", "Lucknow", "Jaipur", "Patna"]

rows = []

for month in months:
    for program in programs:
        for city in cities:
            rows.append({
                "month": month.strftime("%Y-%m"),
                "program": program,
                "city": city,
                "beneficiaries": random.randint(80, 300),
                "funds_spent": random.randint(30000, 120000),
                "volunteers": random.randint(5, 25),
                "sessions_conducted": random.randint(8, 30),
                "dropouts": random.randint(2, 20)
            })

df = pd.DataFrame(rows)
df.to_csv("ngo_data.csv", index=False)
print(df.shape)
print(df.head())