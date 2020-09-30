import pandas as pd
import sys
def bank_code():
    '''将Excel中的资方编码和资方名称转化为一个字典'''
    path = 'D:\zlm\code\zvfp\interface\data\\bank_info.xlsx'
    data = pd.read_excel(path)
    my_dict = data.set_index("bank_name").to_dict()['bank_code']
    return my_dict

if __name__ == '__main__':
    print(bank_code())