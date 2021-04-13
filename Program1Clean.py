import pandas as pd
import numpy as np
# Read the CSV file
netflix_data= pd.read_csv("netflix_titles.csv")
#print the first five rows

print(netflix_data.head())
#print the shape of the data
print(netflix_data.shape)

#anything missing
missing_values_count = netflix_data.isnull().sum()
print(missing_values_count[0:5])

#Drop the missing rows
#droprows= netflix_data.dropna()
#print(netflix_data.shape,droprows.shape)

#dropcolumns = netflix_data.dropna(axis=1)
#print(netflix_data.shape,dropcolumns.shape)

#Fill all missing data with a zero
#cleaned_data = netflix_data.fillna(0)
#Cleaned_data = netflix_data.fillna(method='bfill', axis=0).fillna(0)

#Drop duplicate rows
#drop_duplicates= netflix_data.drop_duplicates()
#print(netflix_data.shape,drop_duplicates.shape)

#Drop duplicate columns
#drop_duplicates= netflix_data.drop_duplicates(subset=['show_id'])
#print(netflix_data.shape,drop_duplicates.shape)

