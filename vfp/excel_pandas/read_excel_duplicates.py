import  pandas as pd
'''
title：读取excel表格，并去除重复的行数据
author：张来明
date：2020-01-19
'''
#解决列名不对齐问题
pd.set_option('display.unicode.ambiguous_as_wide',True)
pd.set_option('display.unicode.east_asian_width',True)
#解决数据显示不全，设置数据列数和宽度
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)
aa = 'D:\zlm\code\\vfp\excel_pandas\data\data-1.xlsx'
#read_excel()函数读取excel表格数据
df = pd.DataFrame(pd.read_excel(aa))
#判断每一行数据是否重复,返回FALSE表示不重复，True表示重复
df.duplicated()
#去除全部重复的数据
df1= df.drop_duplicates()
#去除指定列重复数据
df2 = df.drop_duplicates(['买家应付金额'])
#保留重复行中最后一行。keep='first'取第一行，keep='last'取最后一行，keep=False删除所有重复()
df3 = df.drop_duplicates(['买家应付金额'],keep=False)
print(df3)