import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

file_path = './olm-analysis/py_analysis_quick_start/IMDB-Movie-Data.csv'
df = pd.read_csv(file_path)

# print(df.info())
# print(df.head(1))

print(df["Rating"].mean())
# print(len(set(df["Director"].tolist())))
print(len(df["Director"].unique()))

# 统计演员
tmp_actor_list = df["Actors"].str.split(", ").tolist()
actors_list = [i for j in tmp_actor_list for i in j]
# actors_list = list(np.array(tmp_actor_list).flatten())
print(len(set(actors_list)))

runtime_data = df["Runtime (Minutes)"].values
max_runtime = runtime_data.max()
min_runtime = runtime_data.min()
num_bin = (max_runtime - min_runtime)//5

plt.figure(figsize=(20, 8), dpi=80)
# plt.hist(runtime_data, num_bin)
# plt.xticks(range(min_runtime, max_runtime+5, 5))

# plt.show()

# 统计分类列表
tmp_list = df["Genre"].str.split(",").tolist()
genre_list = list(set([i for j in tmp_list for i in j]))
print(genre_list)
zeros_df = pd.DataFrame(np.zeros((df.shape[0], len(genre_list))), columns=genre_list)
print(zeros_df)

# 电影分类出现位置赋值 1
for i in range(df.shape[0]): # shape (1000, 12)， 1k 行 10 列， 循环 1k 次
    zeros_df.loc[i, tmp_list[i]] = 1

print(zeros_df.head(3))

# 统计分类数量
genre_count = zeros_df.sum(axis=0)
print(genre_count)

# 排序
genre_count = genre_count.sort_values()
# 画图
_x = genre_count.index
_y = genre_count.values
plt.bar(_x, _y)
plt.show()

print("*"*10)
print(df)
print(df.shape)
print(df.shape[0])