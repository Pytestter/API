import pandas as pd
'''
title：读取excel表格数据,进行行列转换
author：张来明
date：2019-11-20
'''
#解决列名不对齐问题
pd.set_option('display.unicode.ambiguous_as_wide',True)
pd.set_option('display.unicode.east_asian_width',True)
#解决数据显示不全，设置数据列数和宽度
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)
#文件目录
path = 'D:\zlm\code\\vfp\excel_pandas\data\data.xlsx'
resultfile = 'D:\zlm\code\\vfp\excel_pandas\data\data-2.xlsx'
#read_excel()函数读取excel表格数据
df = pd.DataFrame(pd.read_excel(path))
df1 = df[['订单付款时间','买家会员名','买家实际支付金额']]
#将“订单付款时间”设置为索引
df1 = df1.set_index('订单付款时间')
#按季度统计并显示
Q_df = df1.resample('Q').sum().to_period('Q').T
print(Q_df)  #输出结果
Q_df.to_excel(resultfile) #导出结果
