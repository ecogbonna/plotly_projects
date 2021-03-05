from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

#Preparing the data
die_1 = Die()
die_2 = Die()
die_3 = Die()

results = []
for i in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#visualizing the data
x_values = list(range(3, max_result+1))
y_values = frequencies
data = [Bar(x=x_values, y=y_values)]

x_axis_config = {'title': 'Results', 'dtick': 1}
y_axis_config = {'title': 'Frequencies of the Results'}
my_layout = Layout(title="Simulation of three six-sides dice", 
    xaxis=x_axis_config, yaxis=y_axis_config)

#plotting
offline.plot({'data': data, 'layout': my_layout}, filename='three_d6.html')

