# -*- coding: utf-8 -*-
"""PreprocessingProjekt.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MEsHrFiIa14h8RcXNh5ehHZmQpJypdx8
"""

# Project PART ONE (Data preparation script)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data and save into DataFrame
file_path = 'dane_eurusd.csv'
df = pd.read_csv(file_path, nrows=2500)

# Drop the 'SMA14IND' and 'SMA50IND' columns
columns_to_drop = ['SMA14IND', 'SMA50IND']
df = df.drop(columns=columns_to_drop)

# Count and print the number of empty rows in 'Close' column
empty_rows = df['Close'].isnull().sum()
print(f"Number of empty rows in 'Close' column: {empty_rows}")

# Fill empty cells with an average of the preceding and succeeding cells
df['Close'] = df['Close'].astype(float)  # Convert to float

mask = df['Close'].isnull()
#df['Close'][mask] = (df['Close'].shift() + df['Close'].shift(-1)) / 2
df['Close'][mask] = df['Close'].interpolate()

# Convert 'column' empty rows based of the preceding cells function
def convert_empty(column,print_results,replace_type):
  empty_rows = 0
  for i in range(1, len(df[column]) - 1):
    if pd.isnull(df[column][i]):
        empty_rows +=1
        if(replace_type == 1):
          df[column][i] = df[column][i-1]
        else:
          df[column][i] = 0

  if(print_results == 1):
    print(f"Number of empty rows in '{column}' column: {empty_rows}")

# Convert 'SMA50' and 'SMA14' empty rows based of the preceding cells
convert_empty('SMA14',1,1)
convert_empty('SMA50',1,1)

# Convert rest of the empty rows in columns 'Bulls', 'CCI', 'DM', 'OSMA', 'RSI', 'Stoch' with zeros
convert_empty('Bulls',1,0)
convert_empty('CCI',1,0)
convert_empty('DM',1,0)
convert_empty('OSMA',1,0)
convert_empty('RSI',1,0)
convert_empty('Stoch',1,0)

# Calculate and print correlation between SMA14 and SMA50
corr_sma14_sma50 = df['SMA14'].corr(df['SMA50'])
print(f"Correlation between SMA14 and SMA50: {corr_sma14_sma50}")

# Calculate correlation between Close and SMA14
corr_close_sma14 = df['Close'].corr(df['SMA14'])
print(f"Correlation between SMA14 and Close: {corr_close_sma14}")

# Calculate correlation between Close and SMA50
corr_close_sma50 = df['Close'].corr(df['SMA50'])
print(f"Correlation between Close and SMA50: {corr_close_sma50}")

# Delete the column where the correlation is highest
if max(corr_close_sma14, corr_close_sma50) == corr_close_sma14:
    df = df.drop(columns=['SMA14'])
    print("Deleting 'SMA14'collumn")
else:
    df = df.drop(columns=['SMA50'])
    print("Deleting 'SMA50'collumn")

# Number of negative elements for 'CCI'
negative_cci_count = (df['CCI'] < 0).sum()
print(f"Number of negative elements for 'CCI': {negative_cci_count}")

# Information about the maximum and minimum values for each attribute
attribute_stats = df.describe().transpose()[['min', 'max']]
print("Information about the maximum and minimum values for each attribute: ")
print(attribute_stats)

# Normalize 'column' function
def normalize(dataframe,column):
    dataframe[column] = (dataframe[column] - dataframe[column].min()) / (dataframe[column].max() - dataframe[column].min())

# Discretize 'column' function
def discretize(dataframe,column,number,labels):
    dataframe[column] = pd.cut(dataframe[column], bins=number, labels=labels)

# Normalize and Discretize 'Close' column
normalize(df,'Close')
normalize(df,'Bulls')

discretize(df,'Close',2,False)
discretize(df,'Bulls',4,False)

# Count each unique value in the 'Decision' column
decision_counts = df['Decision'].value_counts()

# Make a pie chart using 'matplotlib'
plt.figure(figsize=(8, 8))
plt.pie(decision_counts, labels=decision_counts.index, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightgreen', 'lightcoral'])
plt.title('Distribution of Decisions')
plt.show()

# Make a line chart for 'Close' column
plt.figure(figsize=(10, 6))
plt.plot(df['Close'], label='Close')
plt.title('Line Chart for Close')
plt.xlabel('Index')
plt.ylabel('Close Value')
plt.legend()
plt.grid(True)
plt.show()

# Save DataFrame to a JSON
df.to_json('output_eurusd.json', orient='records')

print("Success part #1 \n")

# Project PART THREE (Suggestion of solutions for data preparation)

'''
PL:
Dane są trzy zestawy danych obejmujące około 17.2 tysięcy obietków (nazwa_zestawu.csv). Zestaw ten składa się z 12 różnych
kolumn, z czego wiele z nich wykazuje się dużym współczynnikiem korelacji między sobą. Zdarzają się wartości puste.
Wszystkie kolumny z wyjątkiem 'Decision' są to wartości liczbowe, ostatnie pole odnosi się bowiem do procesu decyzyjnego,
którego ma dotyczyć dany zestaw uczący...

W ramach proponowanych rozwiązań należy wymienić nadpisanie wartości pustych wartościami średnimi lub zerowymi [funkcja .interpolate,
lub ręcznie z użyciem .shift albo dyskretnego indeksowania...], pozbycie się potencjalnych wartości nieliczbowych w wieszach [funkcja
.to_numeric albo .astype]. Po sprawdzeniu poprawności danych można przejść do liczenia współczynników korelacji między kolumnami w
celu pozbycia się kolumn, których obecność w uczeniu nie przełoży się na wymierne korzyści względem pozostałych danych [funkcja .corr].
Ostanim proponowanym etapem przygotowania danych jest normalizacja oraz dyskretyzacja wybranych kolumn (tam gdzie pojawiają się wartości ujemne,
lub przekraczające wartość 1) [funkcje .min, .max oraz .count]. Na końcu warto sprawdzić poprawność przeprowadznych operacji poprzez
narysowanie wykresu/ów lub ręczny odczyt danych.

ENG:
There are three data sets containing approximately 17.2 thousand objects (named_dataset.csv). This set consists of 12 different columns, many of which exhibit high correlation coefficients among them. Empty values occur.
All columns except 'Decision' are numerical values, as the last field refers to the decision-making process concerning the given training set...
As part of the proposed solutions, it is suggested to replace empty values with either mean or zero values [using the .interpolate function, or manually with .shift or discrete indexing...], remove potential non-numeric values in columns [using the .to_numeric or .astype function].
After verifying the correctness of the data, proceed to calculate correlation coefficients between columns to remove columns whose presence in training will not translate into tangible benefits compared to the rest of the data [using the .corr function].
The final proposed step of data preparation is normalization and discretization of selected columns (where negative values appear or exceed the value of 1) [using the .min, .max, and .count functions].
Finally, it is advisable to check the correctness of the performed operations by plotting chart(s) or manually reading the data.

'''

# Project PART TWO (Create new DataFram with artificial data)

# Create new empty DataFrame and reload ori 'df'
df_art = pd.read_csv(file_path, nrows=2500)
df = pd.read_csv(file_path, nrows=2500)

# Rand number seed
np.random.seed(37)

# Generate new column with an artificial data
def generate_column(column):
  for index, value in enumerate(df[column]):
      if index == 0:
          # [min, max]
          df_art.loc[index, column] = np.random.uniform(df[column].min(), df[column].max())
      else:
          # [prev - prev * 1.01, prev + prev * 1.01]
          prev_value = df_art.loc[index - 1, column]
          lower_bound = prev_value - prev_value * 0.01
          upper_bound = prev_value + prev_value * 0.01
          df_art.loc[index, column] = np.random.uniform(lower_bound, upper_bound)

  # Check the correlation between the original and artificiall data
  correlation = df[column].corr(df_art[column])

  # Print the correlation
  print(f"Correlation between df['{column}'] and df_art['{column}']: {correlation}")

# Create artificial columns
generate_column('Close')
generate_column('Bulls')
generate_column('CCI')

print("Success part #2")