import pandas as pd
'''
title：读取excel表格数据,并转化成字典
author：张来明
date：2019-11-20
'''
#文件路径
path = "D:\zlm\code\\vfp\excel_pandas\data-3.xlsx"
df = pd.DataFrame(pd.read_excel(path))
df1 = df.groupby(["宝贝标题"])["宝贝总数量"].sum() #分组统计
df1.to_excel("D:\zlm\code\\vfp\excel_pandas\data\data-4.xlsx")  #保存到excel文件
my_dict = df1.to_dict() #转化为字典
print(my_dict)



