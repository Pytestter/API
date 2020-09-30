import pandas as pd
print("--------------获取文本数据---------------------")
cc = 'D:\zlm\code\\vfp\excel_pandas\data\\fl4_name.txt'
df = pd.read_csv(cc,encoding='utf8')
print(df)