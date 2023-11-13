import matplotlib.pyplot as plt
import seaborn as sns

# 导入鸢尾花数据
iris_sns = sns.load_dataset("iris")
# 绘制花萼长度样本数据直方图
fig, ax = plt.subplots(figsize=(8, 6))

# 纵轴三个选择：stat=频率(count)、概率(probability)、概率密度(density)
sns.histplot(
    ax=ax, 
    data=iris_sns, 
    x='sepal_length', 
    binwidth=0.2, 
    stat='probability',
    hue= 'species'
)

# 增加均值位置竖直参考线
ax.axvline(
    x=iris_sns.sepal_length.mean(), 
    color='r', 
    ls='--'
)

plt.show()