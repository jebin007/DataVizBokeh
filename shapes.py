from bokeh.plotting import figure, output_file, show

output_file('shapes.html')

plot = figure(plot_width=400, plot_height=400, title='Shape')

#the first list is the x-coordinate and the second list is the y-coordinates, alpha is the transperancy value
plot.patch([1, 2, 3, 4], [7, 12, 9, 3], color='#2B5B84', alpha=0.7, line_width=2)

show(plot)