import plotly.express as px

from random_walk import RandomWalk

#preparing data
rw = RandomWalk()
rw.fill_walk()

x_values = rw.x_values
y_values = rw.y_values

fig = px.scatter(x=x_values, y=y_values)
fig.show()



