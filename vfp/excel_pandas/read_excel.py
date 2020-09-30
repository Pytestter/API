import  pandas as pd
'''
title：读取excel表格数据
author：张来明
date：2019-11-20
'''
#文件目录
path = 'D:\zlm\code\\vfp\config_data\\fund_code.xlsx'
#解决数据显示不全，设置数据列数和宽度
pd.set_option('display.max_columns',500)
pd.set_option('display.width',5000)
#数据输出时，列名不对齐问题
pd.set_option('display.unicode.ambiguous_as_wide',True)
pd.set_option('display.unicode.east_asian_width',True)
#read_excel()函数读取excel表格数据
df = pd.DataFrame(pd.read_excel(path))
#选择对应的列进行输出
df1 = df[['fund_code','fund_name']]
print(df1)
