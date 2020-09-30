import json
import random
import os

class GetBankCardNumber(object):
    def __init__(self):
        self.binNum = ""
        self.midNum = ""
        self.lastCode = ""
        self.bankCardNumber = ""

    def getBinNum(self, useRandom=True):
       #print("当前路径 -> %s" % os.getcwd())
        current_path = os.path.dirname(__file__)
        bankToBin = json.load(open(current_path+"/banknametobin.json", encoding="utf-8"))
        bankTocode = json.load(open(current_path+"/bankcode.json", encoding="utf-8"))
        if useRandom:
            #print("随机生成一个银行bin号......")
            #self.bank_name = random.sample(bankToBin.keys(), 1)[0]
            self.bank_name = '建设银行'
            self.binNum = bankToBin[self.bank_name]
            self.bank_code = bankTocode[self.bank_name]
            return self.binNum, self.bank_code, self.bank_name
        else:
            print("请选择银行：")
            bankList = list(bankToBin.keys())
            for i in range(len(bankList)):
                print("%d.%s" % (i, bankList[i]))
            bankNum = input("请输入银行对应的序号:")
            if len(bankNum) == 0:
                return self.getBinNum()
            elif int(bankNum) in range(len(bankList)):
                self.bank_name = bankList[int(bankNum)]
                self.binNum = bankToBin[bankList[int(bankNum)]]
                self.bank_code = bankTocode[bankList[int(bankNum)]]
                return self.binNum, self.bank_code, self.bank_name
            else:
                print("输入有误，请重新输入:")
                return self.getBinNum(useRandom=False)

    def getMidNum(self, useRandom=True):
        #print("默认生成一个16位的银行卡")
        tempMidnum = ""
        for x in range(12):
            tempMidnum = tempMidnum + str(random.randint(0, 9))
            x = x
        self.midNum = tempMidnum
        return self.midNum

    def getLastcode(self, bankNumNoLastcode):
        sum = 0
        for i in bankNumNoLastcode[-1::-2]:
            for m in str(int(i) * 2):
                sum = sum + int(m)
        for j in bankNumNoLastcode[-2::-2]:
            sum = sum + int(j)
        if sum % 10 == 0:
            self.lastCode = '0'
        else:
            self.lastCode = str(10 - sum % 10)
        return self.lastCode

    def getBankCardNumber(self, useRandom=True):
        if useRandom:
            self.getBinNum()
            self.getMidNum()
        else:
            self.getBinNum(useRandom=False)
            self.getMidNum(useRandom=False)
        self.getLastcode(self.binNum + self.midNum)
        self.bankCardNumber = self.binNum + self.midNum + self.lastCode
        return self.bankCardNumber, self.bank_code, self.bank_name
if __name__ == '__main__':
    bank_info = GetBankCardNumber().getBankCardNumber(useRandom=True)
    print(bank_info)




