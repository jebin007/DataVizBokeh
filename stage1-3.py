import numpy as np
import pandas as pd

file = 'country-pops.csv'

countries = pd.read_csv(file, nrows=5)      #nrows=5 limits the data being pulled out to just 5 rows for simplicity
countries_array = np.array(countries.head)

print(countries_array)