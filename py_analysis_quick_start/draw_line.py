from matplotlib import pyplot as plt

# 设置图片 大小 20x8
fig = plt.figure(figsize=(20, 8), dpi=80)

x = range(2, 26, 2)
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 24, 22, 18, 15]

plt.plot(x, y)

# 显示 x 刻度
_xtick_labels = [i/2 for i in range(4, 49)]
plt.xticks(_xtick_labels[::3])

# 显示 y 刻度
plt.yticks(range(min(y), max(y)+1))

# 保存
# plt.savefig('./line01.png')

# 展示
plt.show()