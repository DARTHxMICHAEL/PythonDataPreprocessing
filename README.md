# PythonDataPreprocessing
Simple preprocessing of stock market indicators in Python

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


![pobrany plik (1)](https://github.com/DARTHxMICHAEL/PythonDataPreprocessing/assets/30693125/d050c90f-1a63-441c-af3c-9fa445615e5d)

![pobrany plik](https://github.com/DARTHxMICHAEL/PythonDataPreprocessing/assets/30693125/f049aa08-8759-43af-b550-47d2548d8d34)
