import plotly.express as px

df = px.data.iris()

fig = px.imshow(df.iloc[:, 0:-2],   # 通过 iloc 切片选择了数据帧所有行和除了倒数第一、二列之外的所有列
                text_auto=False,    # 禁用了自动生成文本标签
                width=600,
                height=600,
                x=None,             # 横轴上不显示具体的数值
                zmin=0, zmax=8,      # 颜色映射的范围
                color_continuous_scale='viridis')   # 颜色映射使用的是viridis色谱

# 更新布局设置
fig.update_layout(yaxis=dict(tickmode='array', tickvals=[]))  # 隐藏纵轴刻度标签

# 设置横轴标签
x_labels = ['Sepal length', 'Sepal width',
            'Petal length', 'Petal width']
# 计算列表长度
x_ticks = list(range(len(x_labels)))
# 更新fig对象横轴设置
fig.update_xaxes(tickmode='array', tickvals=x_ticks, ticktext=x_labels)

fig.show()
