import plotly.graph_objects as go
import numpy as np

# 生成随机游走数据
num_steps = 300
t = np.arange(num_steps)
x = np.cumsum(np.random.standard_normal(num_steps))
y = np.cumsum(np.random.standard_normal(num_steps))
z = np.cumsum(np.random.standard_normal(num_steps))

data = go.Scatter3d(
                x=x,
                y=y,
                z=z,
                marker=dict(size=4, color=t, colorscale='Viridis'),
                line=dict(color='darkblue', width=2))

fig = go.Figure(data=data)
fig.update_layout(width=800, height=700)
fig.show()