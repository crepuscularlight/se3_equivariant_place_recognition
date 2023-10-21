import pandas as pd

filepath="/home/liudiyang/Downloads/kitti-20231017T200730Z-001/kitti/kitti_00_database_evaluate_new.pickle"
obj = pd.read_pickle(filepath)

print(obj)