
import pandas as pd

from bokeh.io import output_file, show
from bokeh.plotting import ColumnDataSource, figure

output_file('pop-life.html')

file = 'country-pops.csv'

countries = pd.read_csv(file, nrows=5)      #nrows=5 limits the data being pulled out to just 5 rows for simplicity

country_data = ColumnDataSource(countries)

plot = figure(x_axis_label='Population', y_axis_label='Life Expectancy')
plot.circle(x='Population', y='Life_expectancy', source=country_data, size=15)          #x and y values are column headers in the csv file stored inside the variable country_data

show(plot)
