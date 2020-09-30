import pandas as pd

def fund_code():
    '''将Excel中的资方编码和资方名称转化为一个字典'''
    path = 'D:\zlm\code\\vfp\config_data\\fund_code.xlsx'
    data = pd.read_excel(path)
    my_dict = data.set_index("fund_code").to_dict()['fund_name']
    return my_dict

