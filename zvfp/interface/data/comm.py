'''
vfp各个接口参数数据
author:张来明
date:20191023
version:python3.6.5
'''
from luyou_pre_approval import *
from MongoClient import *
import random
import time


#初始化请求数据
def init_data(fund_code,product_code,capital_package_id,id_number,name):
    chushihua_data ={
        "fundCode":fund_code,
        "transactionId":"zlmchushihua" + base_data.data,
        "productCode":product_code,
        "capitalPackageId":capital_package_id,
        "idNumber":id_number,
        "customerName":name
    }
    return chushihua_data
#文件上传请求数据
def document_upload_data():
    document_upload_data = {
        "batchSize": 1,
        "batchNo": None,
        "list": [{
            "transactionId": "zlmwenjianpost" + base_data.data,
            "threadId": "UyMtMDZfIy1fLUI0MlI0OC1ZX18=",
            "fundCode": "FDCD000038",
            "bid": "19061102",
            "listFile": [{
                "fileType": "IMTP000140",
                "extensionType": ".pdf",
                "fileId": "28201511",
                "vfpUrl": "/upload/In/FDCD000038/20200115/IMTP000140/维仕线下担保函_20200119123553.pdf",
                "fileName": "维仕线下担保函_20200119123553",
                "uploadDate": "20200115",
                "remark": "担保函"
            }, {
                "fileType": "IMTP000140",
                "extensionType": ".pdf",
                "fileId": "28201512",
                "vfpUrl": "/upload/In/FDCD000038/20200115/IMTP000140/维仕线下担保函_20200119123553-1.pdf",
                "fileName": "维仕线下担保函_20200119123553-1",
                "uploadDate": "20200115",
                "remark": "担保函"
            }]
        }]
    }
    return  document_upload_data
#文件下载请求参数
def documet_obtain_data(fund_code,thread_id):
    ducument_obtain_data = {
      "batchSize": 1,
      "batchNo": None,
      "list": [{
        "transactionId": "zlmfilobtain" + base_data.data + "1",
        "fundCode": fund_code,
        "threadId":thread_id,
        "bid": "1292684",
        "fileType": "IMTP000007",
        "fileId":"441595110",
        "fileName": "21349922_个人借款合同.pdf"
      }]
    }
    return ducument_obtain_data


def loan_data(loan_list):
    #通过传入thread，查询数据库
    results = Mongo(loan_list[1]).query_pre_approval_result(loan_list[2])
    loan_data ={
        "maxWaitMillis": 0,
        "batchNo": 'testbatchno'+str(random.randint(100000,2000000)),
        "batchSize": 1,
        "instructions": [{
            "bid":str(random.randint(100000,2000000)),
            "threadId":  results.get('thread_id'),
            "customerType": None,
            "accountCategory": 0, #AUTP000001
            "productCode": None,
            "transactionId": "testloaninstruction"+str(random.randint(1000000,10000000)),
            "sequenceNumber": None,
            "projectCode": None,
            "customerName": results.get('customer_name'),
            "idType": "CETP000001",
            "idNumber": results.get('id_no'),
            "mobilePhone": results.get('mobile_phone'),
            "loanAmount": results.get('apply_amount'),
            #"loanAmount": "10000",
            "loanCurrency": None,
            "accountName": results.get('customer_name'),
            "bankCardNo":  results.get('bank_card_no'),
            "bankCode": results.get('bank_no'),
            "channelCode": loan_list[3],
            "ProductCode": None,
            "fundingUsage": "LUCS000007",
            "bankProvince": None,
            "bankCity": None,
            "extensions": {
                "bankName": results.get('bank_name'),
                "loanPeriod":results.get('apply_period'),
                "marrStatus":"MAST000001",
                "eduDegree":"EDBK000009",
                "repayment": {
                    "dueDay": "09",
                    "mode": "10",
                    "payAcctName": results.get('customer_name'),
                    "payAcctCard": "6225882270039826",
                    "payAcctNo": "308584000013"
                },
                "contract": {
                    "baseRate": None,
                    "rateMode": "FX",
                    "rateMethodRATEMETHOD": None,
                    "rate": "9.0000000",
                    "period": "9",
                    "loanterm2": None,
                    "nxtIntRatChgOpt": "FX",
                    "fixRateInd": "Y",
                    "floatRate": 0.0
                },
                "cbhbOthers": {
                    "loanPurPoseName": None,
                    "channelId": "66",
                    "bankLoanAmt": 18000.0,
                    "loanApplDate": "0001-01-01",
                    "partnerCode": "NLP12",
                    "partnerName": "维信金科",
                    "partnerLoanAmt": 180.0,
                    "trdPbocQueryNo": "DDQ181300020019000029",
                    "signMessage": None,
                    "signType": "30",
                    "termType": "M",
                    "typeNo": "NLP12001",
                    "wdSerialNo": "20200609000002"
                },
                "loanInfo":{
                    "totalCnt":6
                },
                "spouseInfo":{
                    "spouseName":None
                },
                "appTime":"2020-05-22T14:19:55.916",
                "custType":"03",
                "appCity":"340800",
                "contactPhoneNum":"13636659856,13917881831,13341613113",
                "FirstUTLine":"50000.00",
                "FirstUTtime":"2020-05-22T14:19:55.916",
                "currLine":"20000.00",
                "loanTime":"2020-05-21T16:59:06.000"
            }
        }]
    }
    return  loan_data
# data =loan_data('fund_uat','IyVTVzJCUi1GTCVTSzNfMVI4X18=','byincf')
# print(data)

#改卡请求参数 15623910002
def bank_update_data(thread_id,bid):
    bank_update_data = {
     "transactionId":"testupdatebank8353345" + base_data.data,
     "threadId":thread_id,
     "newBankAcName":"笑三笑",
     "bid":bid,
     "newBankNo":"102100099996",
     "newMobile":"17755550001",
     "newBankName":"工商银行",
     "newBankCardNumber":"6212261735856456025",
     "newBankType":"BCTP000001",
     "extensions":{
      "repayBankCode":"102100099996",
      "repayBankName":"工商银行",
      "oldBankNo":"105100000017",
      "oldBankCardNumber":"6227000772298585140",
      "oldBankName":"建设银行",
      "oldMobile":"17933330050",
     }}
    return bank_update_data

#放款取消请求参数
def loan_cancel_data(thread_id):
    loan_cancel_data = {
      "transactionId":"loancancel" + base_data.data,
      "threadId":thread_id,
      "reason":"不要了",
      "extensions":{
        "approval":"1"
      }
    }
    return loan_cancel_data

#放款对账数据
def loan_reconciliation_data(channel_code,date):
    loan_reconciliation_data ={
     "channelCode":channel_code,
     "category":"loan",
     "toDate":date,
     "fromDate":date
    }
    return loan_reconciliation_data
#还款试算数据
def repay_calculate_data(apply_period,bid,planAmount,productCode):
    repay_calculate_data= {
    "repayMode": "RPTP000001",
    "transactionId": "testcalculate" + base_data.data,
    "repayScheduTerm": apply_period,
    "bid": bid,
    "planAmount": planAmount,
    "productCode":productCode
}
    return repay_calculate_data

#代扣数据
def deduct_data():
    deduct_data = {
	"batchNo": base_data.data,
	"batchSize": 1,
	"fundCode": "FDCD100002",
	"channelCode": "zyxj",
	"instructionList": [{
		"bid": "1023718",
		"productCode": "PDCD000032",
		"settlementAccounts": None,
		"contractNo": None,
		"externalContractNo": None,
		"transactionId": "testdeduct" + base_data.data,
		"protocolNo": None,
		"repayPeriod": -1,
		"repayType": "RPTP000002",
		"customerName": "汪小菲",
		"idType": "CETP000001",
		"idNo": "610430197712024090",
		"mobilePhone": "17721362586",
		"bankCode": "ICBC",
		"bankCard": "6230621683708268635",
		"bankProvince": None,
		"deductAccountType": "ACTP000003",
		"bankCity": None,
		"repayAmount": 5000,
		"repayRequestDate": "2024-05-10 19:30:00",
		"subjectList": [{
			"subjectType": "SBJT002001",
			"subjectAmount": 5000,
			"subjectProperty": "SBPR000001"
		}, {
			"subjectType": "SBJT002002",
			"subjectAmount": 0,
			"subjectProperty": "SBPR000001"
		}],
		"extensions": None
	}]
}
    return deduct_data

#还款推送数据
def repay_info_data():
    repay_info_data= {
    "batchNo": "1133ed042c0e4c34af0d0cd0626821e3" ,
    "batchSize":1,
    "fundCode": "FDCD100002",
    "repayList":[
        {"bid": "21350512",
          "repayDetails":[{"seq":1,
                           "termNo":1,
                           "paidDate":"2024-08-13",
                           "repayType":"RPTP000001",
                           "totalAmount": 2205.28,
                           "principalAmount": 1833.28,
                           "interestAmount": 372.00,
                           "repayCardNo":"6236601780837455",
                           "repayCardMobile":"13890550001",
                            "otherFees": {"SBJT002059": "0"}  #还款失败费
                           }]
         }]}
    return repay_info_data
#签约数据
def vbs_sign_data(thread_id):
    results = Mongo('fund_uat').query_pre_approval_result(thread_id)
    vbs_sign_data = {
    "applyId": "testzlmsign" + base_data.data,
    "bankCode": "ICBC",
    "contractSubject": "CYCFC",
    "channelCode": "DEFAULT",
    "merchantId": "",
    "accountNo": results.get('bank_card_no'),
    "accountName": results.get('customer_name'),
    "accountType": "CT00",
    "documentType": "D001",
    "documentNumber": results.get('id_no'),
    "mobilePhone": results.get('phone_no'),
    "waitForVerification": 1,
    "extension": ""
 }
    return vbs_sign_data

#签约确认
def test_sign_verify(applyId):
    test_sign_verify ={
        "applyId": apply_Id,
        "verificationCode": "123456"
    }

#撞库
def test_pre_check(phone,id_no,name):
    test_pre_check= {
        "productCode":"zyxj",
        "phoneNo":phone,
        "idCardNo":id_no,
        "customerName":name,
    }
    return test_pre_check

#协议查询
def agreement_query(id_no,name,bank_card_no,phone):
    agreement_query_data = {
        "applyNo":None,
        "transactionId":None,
        "productCode":"zyxj",
        "agreementType":"3",
        "idCardNo":id_no,
        "customerName":name,
        "bankCardNo":bank_card_no,
        "phoneNo":phone,
        "extensions":None
    }
    return agreement_query_data

def agreement_query1():
    agreement_query_data = {
        "applyNo": None,
        "transactionId": None,
        "productCode": "zyxj",
        "agreementType": "3",
        "idCardNo": "610430197712024090",
        "customerName": "汪小菲",
        "bankCardNo": "105100000017",
        "phoneNo": "17721362586",
        "extentions":{
            "applyAmount":"500000",
            "applyPeriod":"3",
            "purposeArea":"LUCS000004"}
        }
    return agreement_query_data

#授信申请
def pre_apply_data():
    pre_apply_data = {
        "transactionId":"testprepply" + base_data.data,
        "processId":"482340982309428",
        "registerId":"",
        "vcreditCustId":"",
        "productCode":"zyxj",
        "loanInfo":"",
    }

if __name__ == '__main__':
    res = vbs_sign_data('VVVWXyM1XzlJNThKQyNfNjItQSU=')
    print(res)
