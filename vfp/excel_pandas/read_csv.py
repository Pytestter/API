import  pandas as pd
'''
title：读取csv表格数据
author：张来明
date：2019-11-20
'''
bb = 'D:\zlm\code\\vfp\excel_pandas\data\\00001.csv'
#解决数据显示不全，设置数据列数和宽度
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)
#数据输出时，列名不对齐问题
pd.set_option('display.unicode.ambiguous_as_wide',True)
pd.set_option('display.unicode.east_asian_width',True)
df = pd.read_csv(bb,encoding='gbk')
df1 = df[['data','open','high','close','low']]
df1.columns = ['日期','开盘价','最高价','闭市价','最低价']
print(df1)
