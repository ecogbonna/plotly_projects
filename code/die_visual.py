from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

die = Die()
results = []

for i in range(1,1000):
    result = die.roll()
    results.append(result)

frequencies = []

for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#preparing the data
x_values = list(range(1, die.num_sides+1))
y_values = frequencies
data = [Bar(x=x_values, y=y_values)]

#configuring the layout
x_axis_config = {'title': 'Roll of a die'}
y_axis_config = {'title': 'Frequencies of the outcome'}
my_layout = Layout(title='Simulation of a die', 
    xaxis=x_axis_config, yaxis=y_axis_config)

#plotting
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')



