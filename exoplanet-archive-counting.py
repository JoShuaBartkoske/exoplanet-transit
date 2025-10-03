'''
exoplanet_archive_counting.py count up unique stars from csv
author; Joshua Thomas Bartkoske
DoC: Oct 3, 2025
'''

# imports
import os
import pandas as pd

directory = "/Users/joshuabartkoske/exoplanet-transit/archive-files"
file_name = "PS_2025.10.03_10.05.09.csv"
file_path = os.path.join(directory, file_name)

# open file
df = pd.read_csv(file_path, header=105)

# count unique number of host stars
print(len(df["hostname"].unique()))

# filter based off of rotational velocity
fast = 35 # km/s
fast_stars = df[df['st_vsin'] > fast]
print(fast_stars.head())

print(len(fast_stars["hostname"].unique()))
