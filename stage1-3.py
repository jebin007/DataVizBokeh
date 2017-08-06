
import pandas as pd

from bokeh.io import output_file, show
from bokeh.plotting import ColumnDataSource, figure
from bokeh.models import CategoricalColorMapper, HoverTool
from bokeh.layouts import column, row

output_file('pop-life.html')

file = 'country-pops.csv'

countries = pd.read_csv(file)      #nrows=5 limits the data being pulled out to just 5 rows for simplicity

country_data = ColumnDataSource(countries)

color_mapper = CategoricalColorMapper(factors=['Asia','Africa','Antarctica','Australia','Central America','Europe','North America', 'Oceania', 'South America'],
                                      palette=['#00FF00', '#FFD343', 'darkgrey', 'brown', 'cyan', 'crimson', 'red', '#0000FF', 'purple']
                                      )

TOOLTIPS = 'pan, wheel_zoom, box_zoom, reset, hover, save'

#Population vs Life Expectancy
plot_life_expect = figure(x_axis_label='Population', y_axis_label='Life Expectancy', tools=TOOLTIPS, title='Population vs Life Expectancy')
plot_life_expect.diamond(x='Population', y='Life_expectancy', source=country_data, size=10, color=dict(field='Continent', transform=color_mapper), legend='Continent')          #x and y values are column headers in the csv file stored inside the variable country_data

#Population vs Birth Rate
plot_birth_rate = figure(x_axis_label='Population',
                         y_axis_label='Life Expectancy',
                         tools=TOOLTIPS,
                         title='Population vs Birth Rate'
                        )
#Population vs Death Rate
plot_death_rate = figure(x_axis_label='Population',
                         y_axis_label='Life Expectancy',
                         title= 'Population vs Death Rate',
                         tools=TOOLTIPS
                        )

#Plot Population vs Birth Rate
plot_birth_rate.circle(x='Population', y='Birthrate', source=country_data, size=10, color=dict(field='Continent', transform=color_mapper), legend='Continent')  #field='Continent' makes our legend continent.

#Plot Population vs Death Rate
plot_death_rate.triangle(x='Population', y='Deathrate', source=country_data, size=10, color=dict(field='Continent', transform=color_mapper), legend='Continent')


hover = plot_life_expect.select_one(HoverTool)

hover.tooltips = [('Country Name English', '@Country_English'),
                  ('Population', '@Population'),
                  ('Life Expectancy (years)', '@Life_expectancy'),
                  ]                 #The name after @ is a name of the column in the database.

#Hover Data for Population Vs Birth Rate
hover1= plot_birth_rate.select_one(HoverTool)

hover1.tooltips = [('Country Name English', '@Country_English'),
                  ('Population', '@Population'),
                  ('Birth Rate', '@Birthrate')]

#Hover Data for Population vs Death Rate
hover2= plot_death_rate.select_one(HoverTool)

hover2.tooltips = [('Country Name English', '@Country_English'),
                  ('Population', '@Population'),
                  ('Death Rate', '@Deathrate')]

plot_life_expect.legend.location = 'bottom_right'
plot_life_expect.legend.background_fill_color = 'lightgrey'

#Associating multiple plots with xrange
plot_birth_rate.x_range = plot_life_expect.x_range      #Associating birth rate with life expectancy
plot_death_rate.x_range= plot_life_expect.x_range       #Associating death rate with life expectancy

show(row(column(plot_life_expect, plot_birth_rate), column(plot_death_rate)))   #Shows two columns of data: 1st for plot, plot_birth_rate and 2nd for plot_death_rate
