import plotly.express as px

df = px.data.iris()

fig = px.imshow(df.iloc[:, 0:-2],
                text_auto=False,
                width=600,
                height=600,
                x=None,
                zmin=0,zmax=8,
                color_continuous_scale='viridis')

fig.update_layout(yaxis=dict(tickmode='array', tickvals=[]))

x_labels=['Sepal length', 'Sepal width',
          'Petal length', 'Petal width']

x_ticks = list(range(len(x_labels)))

fig.update_xaxes(tickmode ='array', tickvals = x_ticks, ticktext = x_labels)
fig.show()
