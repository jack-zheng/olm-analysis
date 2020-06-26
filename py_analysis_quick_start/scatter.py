import matplotlib
from matplotlib import pyplot as plt


# 显示中文
# Windows/Linus
font = {'family' : 'MicroSoft Yahei', 'weight': 'bold', 'size': '9'}
matplotlib.rc("font", **font)

# 设置图片 大小 20x8
fig = plt.figure(figsize=(20, 8), dpi=80)

y_3 = [13, 12, 12, 12, 10, 13, 17, 15, 15, 13, 15, 14, 12, 14, 18, 15, 18, 22, 19, 20, 24, 20, 18, 19, 20, 24, 14, 9, 10, 13, 15]
y_10 = [25, 28, 30, 29, 25, 24, 25, 23, 24, 27, 26, 25, 25, 23, 20, 22, 22, 23, 22, 24, 24, 23, 23, 24, 23, 20, 21, 20, 22, 22, 23]

x_3 = range(1, 32)
x_10 = range(51, 82)

plt.scatter(x_3, y_3, label="3月")
plt.scatter(x_10, y_10, label="10月")

# 调整 x 刻度
_x = list(x_3) + list(x_10)
_xtick_labels = ["3月{}日".format(i) for i in x_3]
_xtick_labels += ["10月{}日".format(i) for i in x_10]
plt.xticks(_x[::3], _xtick_labels[::3], rotation=45)

# 添加描述信息
plt.xlabel("时间")
plt.ylabel("温度")
plt.title("3/10月份温度表")

# 添加图列
plt.legend()

plt.show()