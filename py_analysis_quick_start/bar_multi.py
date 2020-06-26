import matplotlib
from matplotlib import pyplot as plt


# 显示中文
# Windows/Linus
font = {'family' : 'MicroSoft Yahei', 'weight': 'bold', 'size': '9'}
matplotlib.rc("font", **font)

# 设置图片 大小 20x8
fig = plt.figure(figsize=(20, 8), dpi=80)

a = ["猩球崛起", "最终之战", "敦刻尔克", "战狼2"]
b_16 = [15746, 312, 4497, 319]
b_15 = [12357, 156, 2045, 168]
b_14 = [2358, 399, 2358, 362]

bar_width = 0.2
x_14 = list(range(len(a)))
x_15 = [i+bar_width for i in x_14]
x_16 = [i+ bar_width*2 for i in x_14]

plt.bar(x_14, b_14, width=bar_width, label="9-14")
plt.bar(x_15, b_15, width=bar_width, label="9-15")
plt.bar(x_16, b_16, width=bar_width, label="9-16")

# 设置 x 刻度
plt.xticks(x_15, a)

# 添加描述信息
plt.xlabel("电影名")
plt.ylabel("票房")
plt.title("票房榜")

plt.grid(alpha=0.3)
plt.legend()

plt.show()