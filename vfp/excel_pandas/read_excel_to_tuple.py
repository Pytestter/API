import pandas as pd
'''
title：读取excel表格数据,并转化成元组
author：张来明
date：2019-11-20
'''
#文件路径
path = "D:\zlm\code\\vfp\excel_pandas\data\data-5.xlsx"
df = pd.DataFrame(pd.read_excel(path))
df1 = df[['label1','label2']]
#使用列表推导式将转化为元组的dateFrame生成列表
tuples = [tuple(x) for x in df1.values]
print(tuples)



