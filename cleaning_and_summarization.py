import pandas as pd
import numpy as np

df = pd.read_csv("ngo_data.csv")

print(df.shape)
print(df.dtypes)
print(df.info())
print(df.head())


df["month"] = pd.to_datetime(df["month"]) # converted from string to datetime
print(df.dtypes)

print(df.describe())

print((df["dropouts"] > df["beneficiaries"]).sum()) # check whether in any row dropouts are greater than beneficiaries, since we can't lose more people than we had => data has a problem

print(df.groupby("city")["funds_spent"].sum())

# Read each line inside .agg() as:
# new_column_name = ("original_column", "what to do with it")


print(df.groupby("city").agg(
    total_beneficiaries = ("beneficiaries", "sum"),
    total_funds = ("funds_spent", "sum"),
    avg_volunteers = ("volunteers", "mean"),
    total_dropouts = ("dropouts", "sum")
))

# dropout rate is more important than dropout
df["dropout_rate"] = df["dropouts"] / df["beneficiaries"]
print(df.head())

# How is each program performing in each city?
# average dropout rate per program
print(df.groupby("program")["dropout_rate"].mean())

program_summary = df.groupby("program").agg(
    avg_dropout_rate = ("dropout_rate", "mean"),
    total_beneficiaries = ("beneficiaries", "sum"),
    total_funds = ("funds_spent", "sum")
)

program_summary["cost_per_beneficiary"] = program_summary["total_funds"] / program_summary["total_beneficiaries"]

print(program_summary.head())


# city level version
city_summary = df.groupby("city").agg(
    avg_dropout_rate = ("dropout_rate", "mean"),
    total_beneficiaries = ("beneficiaries", "sum"),
    total_funds = ("funds_spent", "sum")
)

city_summary["cost_per_beneficiary"] = city_summary["total_funds"]/city_summary["total_beneficiaries"]

print(city_summary.head())

print(df.groupby(pd.Grouper(key="month", freq="QS")).agg(
    total_beneficiaries = ("beneficiaries", "sum"),
    total_funds = ("funds_spent", "sum")
))

print(df.duplicated().sum())

df["sessions_per_volunteer"] = df["sessions_conducted"] / df["volunteers"]
print(df.head())

print(df[["sessions_per_volunteer", "beneficiaries", "dropouts", "dropout_rate"]].corr())

# time to store the cleaned and summarized data to SQLite

import sqlite3
conn = sqlite3.connect("ngo_database.db")
df.to_sql("ngo_clean", conn, if_exists="replace", index=False)

cursor = conn.cursor()
#cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
#print(cursor.fetchall())


program_summary.to_sql("program_summary", conn, if_exists="replace", index=True)
city_summary.to_sql("city_summary", conn, if_exists="replace", index=True)
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print(cursor.fetchall())


result = pd.read_sql("SELECT * FROM ngo_clean WHERE city = 'Lucknow'", conn)
print(result)
result = pd.read_sql("SELECT * FROM program_summary ORDER BY cost_per_beneficiary DESC", conn)
print(result)

conn.close()