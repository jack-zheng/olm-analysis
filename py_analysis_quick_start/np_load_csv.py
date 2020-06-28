import numpy as np

us_file_path = './olm-analysis/py_analysis_quick_start/youtube_video_data/US_video_data_numbers.csv'
uk_file_path = './olm-analysis/py_analysis_quick_start/youtube_video_data/GB_video_data_numbers.csv'

t1=np.loadtxt(us_file_path, delimiter=",", dtype="int")
t2=np.loadtxt(uk_file_path, delimiter=",", dtype="int")

# 取不连续多行
print(t2[[2, 8, 10]])

# 取列
print(t2[:, 0])

# 取连续多列
print(t2[:, 2:])

# 取不连续多列
print(t2[:, [2,3]])

# 多个点(0,0) (2, 1) (2, 3)
print(t2[[0, 2, 2], [0, 1, 3]])