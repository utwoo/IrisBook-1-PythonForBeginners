import numpy as np
import plotly.express as px
import pandas as pd

# 生成横轴数据
x_array = np.linspace(0, 2 * np.pi, 100)
# 正弦函数数据
sin_y = np.sin(x_array)
# 余弦函数数据
cos_y = np.cos(x_array)

df = pd.DataFrame({'x': x_array, 'Sine': sin_y, 'Consine': cos_y})

# 创建图表
fig = px.line(df, x='x', y=['Sine', 'Consine'], labels={'value': 'f(x)', 'X': 'x'})

# 显示图表
fig.show()
