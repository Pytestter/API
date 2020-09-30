import  pandas as pd
'''
title：读取excel表格指定行列。读取数据转化成列表
author：张来明
date：2020-01-14
'''
#解决列名不对齐问题
pd.set_option('display.unicode.ambiguous_as_wide',True)
pd.set_option('display.unicode.east_asian_width',True)
#解决数据显示不全，设置数据列数和宽度
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)
aa = 'D:\zlm\code\\vfp\excel_pandas\data\data.xlsx'
#read_excel()函数读取excel表格数据
df = pd.DataFrame(pd.read_excel(aa))
#1.按行选取数据
#1.1选取第1行数据
df1 = df[0:1]
#1.2选取五行之前的数据
df2 = df[:5]  #方式1
df3 = df.head(5) #方式2
#1.3选取最后一行数据
df4 = df[-1:]
#2.按列选择数据
#2.1选取一列，指定名称
df5 = df['买家会员名']
#2.2选取多列，指定名称
df6 = df[['买家会员名','买家实际支付金额','订单状态']]
#3.按行列综合选取数据
#知识点：
  #1 loc()方法基于列标签，可选取特定行（使用行索引index）
  #2 iloc()方法 基于行/列的位置
  #3 at()方法，根据指定行索引index及列标签，快速定位Dataframe的元素
  #4 iat(）方法，与at类似，不同的是根据position位置类定位的
#3.1知道列名，选取某一行数据,如选取第2，3行的'买家会员名'和'买家实际支付金额'；若只填第1个参数，则是进行“行”选择
df7 = df.loc[[2,3],['买家会员名','买家实际支付金额']]
#3.2如果列名太长，可根据索引
df8 = df.iloc[0:3,[0,3,4,5]]
#3.3选取'买家会员名'列的第3行数据
df9 = df.at[3,'买家会员名']
#4.数据类型转化
#4.1将第一行数据转化为数组
values = df1.values  #将第一行的数据转化为数组
#引用数组中的值
name = values[0][0]
#4.2 将多行数据转化为列表,并使用循环编列列表
print(df2)
values = df2.values
for i in  range(len(values)):
    for j in range(len(values[0])):
        print(values[i][j])




