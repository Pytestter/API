import  os
import json
#通过输入数字,返回对应的product_code
def product_code(default=True):
    ddq_code = 'PDCD000012'
    if default:
        return ddq_code
    else:
        print("="*10+"产品列表"+"="*10)
        product_code_list = json.load(open("D:\zlm\code\资方路由2.0\data\product_code.json", encoding="utf-8"))
        product_list = list(product_code_list)
        for i in range(len(product_list)):
            print("%d: %s"%(i,product_list[i]))
        product_num = input("请出入产品对应的编号:")
        if len(product_num)==0:
            return product_code()
        elif int(product_num) in range(len(product_list)):
            cc_code = product_code_list[product_list[int(product_num)]]
            return  cc_code
        else:
            print("输入有误，请重新输入:")
            return product_code(default=False)

if __name__ == '__main__':
    product_code = product_code(default=False)
