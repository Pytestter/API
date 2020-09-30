import pandas as pd
'''
title：读取excel表格数据,并进行排序
author：张来明
date：2019-11-20
'''
#解决列名不对齐问题
pd.set_option('display.unicode.ambiguous_as_wide',True)
pd.set_option('display.unicode.east_asian_width',True)
#解决数据显示不全，设置数据列数和宽度
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)
path = 'D:\zlm\code\\vfp\excel_pandas\data\data-6.xlsx'
#read_excel()函数读取excel表格数据
df = pd.DataFrame(pd.read_excel(path))
#按照销量降序排列 ascending=False 降序   ascending=True 升序
df1=df.sort_values(by='销量',ascending=False)
#首先按照"图书名称"，再按照"销量"排序
df2 = df.sort_values(by=['图书名称','销量'])
#按“类别”分组统计销量并进行降序排序
df3 = df.groupby(['类别'])["销量"].sum().reset_index()
df4 = df3.sort_values(by='销量',ascending=False)

