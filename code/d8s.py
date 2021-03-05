from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

#preparing the data
die_1 = Die(8)
die_2 = Die(8)

results = []
for i in range(10_000_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#preparing the visualization
x_values = list(range(2, max_result+1))
y_values = frequencies
data = [Bar(x=x_values, y=y_values)]

#configuring the plot
x_axis_config = {'title': 'Results', 'dtick': 1}
y_axis_config = {'title': 'Frequencies of the result'}
my_layout = Layout(title="Simulation of a dice of 8 sides", xaxis=x_axis_config,
    yaxis=y_axis_config)

#plotting
offline.plot({'data': data, 'layout': my_layout}, filename="d8_d8.html")

