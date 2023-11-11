import plotly.express as px

df = px.data.iris()
fig = px.scatter_3d(df,
                    x='sepal_length',
                    y='sepal_width',
                    z='petal_length',
                    size='petal_width',
                    color='species')

fig.update_layout(autosize=False, width=500, height=500)
fig.layout.scene.camera.projection.type = "orthographic"
fig.show()
