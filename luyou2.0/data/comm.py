import time
from MongoClient import *
import random
str_data = str(int(time.time()))
#路由初始化参数
def init_data(id_number,name,product_code):
    init_data = {
		"serviceCode":"init",
		"idCardNo": id_number,
		"customerName":name,
		"idType": "20",
		"pid":"319174329378295808",
		"productCode": product_code,
		"tractionId": "zlmtestchushihua"+str_data,
	}
    return init_data

#路由预筛选参数
def select_data(serviceCode,token,customer_name,id_number,product_code,phone,
				apply_amount,bank_info,supplementCustomerType,customerMark,applyPeriod,sync):
	select_data = {
		"transactionId":"zlmtestselect"+str_data,
		"productCode":product_code,
		"routeAuthToken": token,
		"serviceCode": serviceCode,
		"sync":sync,
		"personalBasicInfo": {
			"idType":"CETP000001",
			"idNo":id_number,
			"idValidStart":"20100802",
			"idValidEnd":"20200929",
			"customerName":customer_name,
			"birthdate":"19740101",
			"customerType":"CTTP000003",
			"email":"965015785@qq.com",
			"sex":"F" if int(id_number[-2])%2==0 else "M",
			"nation":"汉",
			"marriage":"MAST000002",
			"education":"EDBK000003",
			"degree":"DEGR000006",
			"phoneNo":phone,
			"customerSource":"线上",
			"address":"山东省烟台市福山区八角口村011号",
			#"address":"四川省达州市达州区北京西路1号",
			"postAddr":"山东省烟台市福山区八角口村011号",
			"isOldCustomer":"0",
			"isMemberFeeExpired":"0",
			"loanSpecialUserType":"2",
			"channelName":"fhd",         #渠道编号
			"liveVerificationResult":"0",
			"deviceNo": "865371039361513",
			"idIssuingAuthority": "上海市公安局杨浦分局",
			"registerTime": "20171221120000",
			"channelType": "-1"
			},
		"loanApplicationInfo": {
			"applicantType":"APTP000001",
			"applyArea":"上海市",
			"applDate": "2019-01-01",
			"loanType": "ORTP000001",   #贷款类型  1.新贷 2.加贷 3.再贷
			"riskManLoanType": "ROTP000001",  # 1.新贷 2.加贷 3.再贷 4.首贷非首笔
			"creditUpfrontLabel":"-1",
			"lastSettlementDate": "-",
			"loanCurrency": "CURY000001",
			"applyAmount": apply_amount,     #提现金额
			"applyPeriod": applyPeriod,
			"changePeriod":"3",     #变更期数
			"inRate": "0.105",
			"monthlyInterestRate": "0.008500",
			"monthlyServiceRate": "0.008500",
			"highMonthlyRate": "0.02",
			"specialMonthlyRate": "0.02",
			"formalitiesRate": "0",
			"formalitiesFee": "0",
			"deductionAmount": "0",
			"creditChannel": "CRCH000002",
			"creditInfoCacheFlag": "1",
			"creditCheckTime": "20171221145658",
			"creditAmt": "20000.000000",
			"customerLevel": '3' ,
			"creditReportId": "1164018586902069249",  #征信报告Id
			"firstLoanFlag": "1",
			"supplementCustomerType":supplementCustomerType,
			"mobileReportId": "jxl_19802539",
			"repayMethod": "RPMD000001",
			"dueDayOpt": None,
			"purposeArea": "LUCS000009",
			"purpose":"LUTP000006",   #LUTP000005 消费类 #LUTP000006 经营类
			"customerMark": customerMark,
            "maximumAvailableAmount":"50000",
			"repayType":"RPMD000001",
			"reloanCustomerQualification": "特优客户"
			},
		"personalJobInfo": {
			"incomeMonth": "5000",
			"incomeOfYear": "3",
			"occupation":"OCCU000004",   #验证字段  职业
			"accfundstate":"2",   #是否缴纳公积金
			"industry":"INDU000021",
			"companyName":"上海市智慧金融有限公司",
			"companyAddr":"上海市虹口区四川北路",
			"indivEmpTyp":"dadasd",
			#"preSubjectLabel": "5",   #前置费用标签
			"position":"POSI000008",
			"positionalTitle": "POTI000002",
			"indivEmpYrs": "10",
			"indivEmpTel": "3131"
			},
		"bankCardInfo": {
			"bankNo": bank_info[1],
			"bankName": bank_info[2],
			"bankType": "BCTP000001",
			"bankCardNo":bank_info[0],
			"bankBranchName": bank_info[2],
			"bindPhone":phone,
			"repayBankNo": bank_info[1],
			"repayBankCardNo": bank_info[0],
			"repayBindPhone": phone,
			"repayBankName":  bank_info[2],
			"applAcTyp": "AUTP000001",
			"applIdTyp": "CETP000001",
			"applAcKind": "ACTP000001",
			"applAcNam": "张一山",
			"applIdNo": id_number,
			"repayBankType": "BCTP000001",
			"isFourCheck": "1",
			"fourCheckResult": "1",
			},
		"familyInfo": {
			"homeArea": "山东省烟台市福山区八角口村011号",
			"localResident": "HRTP000001",
			"homeInfo": "HSST000013",
			"familyIncomeMonth": "10000",
			"hasChildren": "1",
			"hasCar": "0",
			"hasCarCredit": "1",
			"familyTel": "400211211",
			"familyZip": "412300",
			"housePrice": "100000"
			},
		"contactsInfo": [{
			"contactName": "杨紫",
			"contactRel": "RELA000001",
			"contactMobile": "15514560001",
			"contactIdType": "CETP000001",
			"contactIdNo": "110101197401011894"
			}, {
			"contactName": "陈涛",
			"contactRel": "RELA000002",
			"contactMobile": "15514560002",
			"contactIdType": "CETP000001",
			"contactIdNo": "110101197401011915"
			}],
		"fundSpecialInfo": {
			"referType": "04"
			},
		"idCardImageInfo": {
			 "idFrontImage": "http://10.139.60.163/group1/M01/60/18/Cos8o11cspSAFod8AACO72pQ8oY140.jpg",
			"idBackImage": "http://10.139.60.163/group1/M01/60/18/Cos8o11csmmAZzJFAAR33xq9DTI426.jpg",
			"handUpImage": "http://10.139.60.163/group1/M01/60/18/Cos8o11csr-AFJEbAACXHvIDsGQ282.jpg",
			"livingBodyImage": "http://10.139.60.163/group1/M01/60/18/Cos8o11csr-AFJEbAACXHvIDsGQ282.jpg",
			"signPic": "http://10.139.60.163/group1/M01/60/1A/Cos8o11dF6qAKL-oAABi5feQHFE174.png",
			"signType": None
			},
		"frontControlInfo": {
			"noSettleFundCode": [],
			"maxAuditTimes":"10",
			#"controlFundCode":"FDCD000022",
			#"removedFundCodes":"FDCD000019"
			},
		}
	return select_data

#路由预筛选查询参数
def select_query_data(token):
	select_query_data = {
	"routeAuthToken": token,
	"serviceCode": "prescreenQuery"
	}
	return select_query_data

#预筛选成功后路由
def route_success_data(token,product_code):
	route_success_data = {
		"serviceCode":"routeIgnorePreScreen",
		"routeAuthToken": token,
		"instructionId": None,
		"threadId": None,
		"transactionId": "zlmtestroute"+str_data,
		"transactionTime": None,
		"fundCode": None,
		"orgId": None,
		"productCode": product_code,
		"frontAccountInfo":{
			"guaranteeCompany":"COMPANY/SZZYRZDB_PREFEE",    #担保公司 AMC、 COMPANY/SZZYRZDB_PREFEE、COMPANY/SZRQRZDB_PREFEE
			"frontAccountPayResult":"3",  #前置科目支付结果  1成功, 2失败,3其他
			"frontAccountPayMode":"1",   #前置科目支付模式 1主动支付 2放款前代扣 3放款后代扣 4交单立即扣 999无前置科目
			"frontAccountPayType":"0",  #前置科目缴纳类型 0缴纳 1-7 未缴纳原因
		},
		"idCardImageInfo": {
			"idFrontImage": "http://10.139.60.163/group1/M01/61/2B/Cos8o13D0_SAYK4WAAGC8o4UgIU655.jpg",
			"idBackImage": "http://10.139.60.163/group1/M01/61/2B/Cos8o13D0_SAGzKaAAJcdwOAc5k205.jpg",
			"handUpImage": "",
			"livingBodyImage": "http://10.139.60.163/group1/M01/61/2B/Cos8o13D0_SAPd6oAAAbgxBB0wU453.jpg",
			"signPic": "http://10.139.60.163/group1/M01/61/35/Cos8o13I95qActcyAAA4Zr7uIjE734.png",
			"signType": None
		},
		"extensionDTO": None,
		"riskControlData": None
	}
	return route_success_data

#路由查询数据
def route_query_data(token,id_no,product_code,name,fund_code):
	route_query_data = {
		"routeAuthToken":token,
		"serviceCode":"routeQuery",
		"fundCode":fund_code,
		"idType":"20",
		"idCardNo":id_no,
		"productCode":product_code,
		"customerName":name,
		"pid":"123456789",
		"transactionId":"'testroutequery"+str_data,
	}
	return  route_query_data
# 放款请求参数
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
#签约数据
def sign_data(thread_id):
    results = Mongo('fund_sit2').query_pre_approval_result(thread_id)
    sign_data = {
		"transactionId": "128"+str_data,
		"contractSubject": "CYCFC",
		"applyNo": "test"+str_data,
		"bankCardNo": results.get('bank_card_no'),
		"bankCardType": "BCTP000001",
		#"bankCode":results.get('bank_no') ,
		"bankCode":"ICBC" ,
		"bindName": results.get('customer_name'),
		"idType": "CETP000001",
		"idNo": results.get('id_no'),
		"bindPhone": results.get('phone_no'),
		"channelCode": "PLATFORM"
	}
    return sign_data
#SUBMITTED->COMPLETED
#签约确认
def sign_verify_data(applyNo):
	sign_verify_data = {
		"transactionId": "testverify"+str_data,
		"contractSubject": "CYCFC",
		"applyNo": applyNo,
		"verifyCode": "123456"
	}
	return sign_verify_data



#签约查询
def sign_query(data):
	sign_query_data = {
		"transactionId":"testzlmsighquery"+str_data,
		"contractSubject": "CYCFC",
		"applyNo": data['applyNo'],
		"bankCardNo": data['bankCardNo'],
		"bankCardType": "BCTP000001",
		"bankCode": data['bankCode'],
		"bindName": data['bindName'],
		"idType": "CETP000001",
		"idNo": data['idNo'],
		"bindPhone": data['bindPhone'],
		"channelCode": "PLATFORM"
	}
	return sign_verify_data

if __name__ == "__main__":
	data = sign_data("MlZVTCMwR1Q1VSVONlNfJUNXWUU=")
	print(data)