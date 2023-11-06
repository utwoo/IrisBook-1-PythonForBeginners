import numpy as np
import plotly.express as px

# 从Ploly中导入鸢尾花样本数据
iris_df = px.data.iris()

# 绘制散点图，不渲染marker
fig = px.scatter(iris_df,
                 x='sepal_length', y='sepal_width',
                 width=600, height=600,
                 labels={'sepal_length': 'Sepal length (cm)',
                         'sepal_width': 'Sepal width (cm)'})

# 修饰图像
fig.update_layout(xaxis_range=[4, 8], yaxis_range=[1, 5])
xticks = np.arange(4, 8+1)
yticks = np.arange(1, 5+1)

fig.update_layout(xaxis=dict(tickmode='array',
                             tickvals=xticks))
fig.update_layout(yaxis=dict(tickmode='array',
                             tickvals=yticks))

fig.show()

# 绘制散点图，渲染marker展示鸢尾花分类
fig = px.scatter(iris_df, 
                 x="sepal_length", y="sepal_width",
                 color="species",
                 width = 600, height = 600,
                 labels={"sepal_length": "Sepal length (cm)",
                         "sepal_width": "Sepal width (cm)"})

# 修饰图像
fig.update_layout(xaxis_range=[4, 8], yaxis_range=[1, 5])
fig.update_layout(xaxis = dict(tickmode = 'array',
                               tickvals = xticks))
fig.update_layout(yaxis = dict(tickmode = 'array',
                               tickvals = yticks))

fig.update_layout(legend=dict(yanchor="top", y=0.99,
                              xanchor="left",x=0.01))
fig.show()