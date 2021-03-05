from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

die_1 = Die()
die_2 = Die(10)

#using list comprehension
results = [die_1.roll() + die_2.roll() for i in range(1, 50_000)]

# for i in range(1, 50_000):
#     result = die_1.roll() + die_2.roll()
#     results.append(result)

max_result = die_1.num_sides + die_2.num_sides

#using list comprehension
frequencies = [results.count(value) for value in range(2, max_result+1)]

# for value in range(2, max_result+1):
#     frequency = results.count(value)
#     frequencies.append(frequency)

#preparing the data
x_values = list(range(2, max_result+1))
y_values = frequencies
data = [Bar(x=x_values, y=y_values)]

#configuring the layout
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequencies of Result'}
my_layout = Layout(title='Simulation of d6 and d10 throw 1000 times', 
    xaxis=x_axis_config, yaxis=y_axis_config)

#plotting
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')




