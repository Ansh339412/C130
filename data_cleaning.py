import pandas as pd 
import csv 
df=pd.read_csv("Data_merged.csv")


del df["name.1"]

del df["year_discovered.1"]
del df["discoverer.1"]
del df["distance_from_planet (km).1"]
del df["diameter (km).1"]
del df["orbital_period.1"]
del df["host_planet.1"]

print(df.columns)