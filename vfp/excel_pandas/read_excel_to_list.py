import pandas as pd
'''
title：读取excel表格数据,并转化成列表
author：张来明
date：2019-11-20
'''
#文件路径
path = "D:\zlm\code\\vfp\excel_pandas\\data\data-3.xlsx"
df = pd.DataFrame(pd.read_excel(path))
df1 = df[['宝贝标题']]
#去除重复记录，使用tolist(）方法转成list
list1 = df1['宝贝标题'].drop_duplicates().values.tolist()
print(list1)



