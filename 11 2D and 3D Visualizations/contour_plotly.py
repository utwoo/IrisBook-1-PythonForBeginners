
import numpy as np
import plotly.graph_objects as go # 模块plotly.graph_objects有丰富的可视化方案。

# 创建二维数据
x = np.linspace(-3, 3, 121)
y = np.linspace(-3, 3, 121)
X, Y = np.meshgrid(x, y)
Z = X * np.exp(- X**2 - Y**2)

# 等高线设置
levels = dict(start=-0.5, end=0.5, size=0.05)
data = go.Contour(x=x, y=y, z=Z,                # x,y:一维 z:二维
                  contours_coloring='lines',    # 等高线的着色方式 
                  line_width=2,                 # 定等高线的线宽
                  colorscale='RdYlBu_r', 
                  contours=levels)              # 等高线参数

# 创建布局
layout = go.Layout(width=600,
                   height=600,
                   xaxis=dict(title=r'$x_1$'),
                   yaxis=dict(title=r'$x_2$'))

# 创建图形对象
fig = go.Figure(data=data, layout=layout)

fig.show()
