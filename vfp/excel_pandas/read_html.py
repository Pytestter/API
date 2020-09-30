import pandas as pd
'''
title：读取html表格数据
author：张来明
date：2019-11-20
'''
df = pd.DataFrame()
url_list =['http://www.espn.com/nba/salaries/_/seasontype/4']
for i in range(2,14):
    url = 'http://www.espn.com/nba/salaries/_/page/%s/seasontype/4' %i
    url_list.append(url)
#遍历网页中的table读取网页中的数据
for url in url_list:
    df = df.append(pd.read_html(url),ignore_index=True)
#列表解析，遍历dataFrame第3列，以字符串$开头
df = df[[ x.startswith('$') for x in df[3]]]
df.to_csv('D:\zlm\code\\vfp\excel_pandas\\NABll.csv',header=['RK','NAME','TEAM','SALARY'],index=False)