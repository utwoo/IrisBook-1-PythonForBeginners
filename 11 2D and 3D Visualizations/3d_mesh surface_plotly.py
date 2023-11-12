import plotly.graph_objects as go
import numpy as np

# 生成曲面数据
x = np.linspace(-3, 3, 121)
y = np.linspace(-3, 3, 121)

X, Y = np.meshgrid(x, y)
Z = X * np.exp(-X**2 - Y**2)

# 创建三维曲面图的对象
data = go.Surface(x=x, y=y, z=Z, colorscale='RdYlBu_r')
fig = go.Figure(data=data)

fig.layout.scene.camera.projection.type = 'orthographic'
fig.update_layout(width=800, height=700)
fig.show()
