import matplotlib.pyplot as plt

# 定义二维列表
A = [[0, 5],
     [3, 4],
     [5, 0]]

# 自定义可视化函数
def draw_vector(vector, RGB):
    plt.quiver(0, 0,                # 箭头的起点坐标
               vector[0],           # 箭头在 x 轴上的分量
               vector[1],           # 箭头在 y 轴上的分量
               angles='xy',         # 箭头应该以 x 和 y 轴的角度来表示
               scale_units='xy',    # 箭头的比例应该根据 x 和 y 轴的单位来缩放
               scale=1,             # 箭头的长度应该乘以的比例因子
               color=RGB,           # 箭头的颜色
               zorder=1e5)          # 图层序号


fig, ax = plt.subplots()
v1 = A[0]  # 第一行向量
draw_vector(v1, "#FFC000")
v2 = A[1]  # 第二行向量
draw_vector(v2, "#00CC00")
v3 = A[2]  # 第三行向量
draw_vector(v3, "#33A8FF")

ax.axvline(x=0, c='k', linestyle='--')  # 画一条水平线
ax.axhline(y=0, c='k', linestyle='--')  # 画一条垂直线
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.grid()
ax.set_aspect('equal', adjustable='box')
ax.set_xbound(lower=-0.5, upper=5)
ax.set_ybound(lower=-0.5, upper=5)

plt.show()
