
'''
titile : 资方路由豆豆测试参数
author:张来明
date:20190522
version:python3.7.3
'''
import time
data = str(int(time.time()))

#公共参数
def init_data(id_number,name,product_code,routeAuthToken=None):
	chushihua_data = {
		"serviceCode":"init",
		"idCardNo": id_number,
		"customerName":name,
		"idType": "20",
		"pid":"319174329378295808",
		"productCode": product_code,
		"transactionId": "zlmtestchushihua" + data,
		"routeAuthToken":routeAuthToken
	}
	return chushihua_data
#豆豆钱的预审批入参 20231231		,
def pre_apro_data(pre_list,phone,bank_info):
	yushenpi_data ={
		"transactionId":"zlmtestpre" + data,
		"productCode":pre_list[3],
		"routeAuthToken": pre_list[0],
		#"sync":"True",
		"personalBasicInfo": {
			"idType":"CETP000001",
			"idNo":pre_list[2],
			"idValidStart":"20191212",
			"idValidEnd":"99990101",
			"customerName":pre_list[1],
			"birthdate":"19740101",
			"customerType":"CTTP000003",
			"email":"965015785@qq.com",
			"whiteListType":"-1",
			"sex":"F" if int(pre_list[2][-2])%2==0 else "M",
			"nation":"汉",
			"marriage":"MAST000007",
			"education":"EDBK000001",
			"degree":"DEGR000003",
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
			"applyAmount": pre_list[5],     #提现金额
			"applyPeriod": pre_list[6],
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
			"supplementCustomerType":pre_list[7],
			"mobileReportId": "jxl_19802539",
			"repayMethod": "RPMD000002",
			"dueDayOpt": None,
			"purposeArea": "LUCS000005",
			"purpose":"LUTP000006",   #LUTP000005 消费类 #LUTP000006 经营类
			"customerMark": pre_list[8],
            #"maximumAvailableAmount":"50000",
			"repayType":"RPMD000002",
			"reloanCustomerQualification":"特优客户"
			},
		"personalJobInfo": {
			"incomeMonth": "5000",
			"incomeOfYear": "3",
			"occupation":"OCCU000007",   #验证字段  职业
			"accfundstate":"2",   #是否缴纳公积金
			"industry":"INDU000021",
			"companyName":"上海市智慧金融有限公司",
			"companyAddr":"上海市虹口区四川北路",
			"indivEmpTyp":"其他",
			"preSubjectLabel": "7",   #前置费用标签
			"position":"POSI000003",
			"positionalTitle": "POTI000003",
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
			"repayBankNo":bank_info[1] ,
			"repayBankCardNo":bank_info[0],
			"repayBindPhone": phone,
			"repayBankName":  bank_info[2],
			"applAcTyp": "AUTP000001",
			"applIdTyp": "CETP000001",
			"applAcKind": "ACTP000001",
			"applAcNam": "张一山",
			"applIdNo": pre_list[2],
			"repayBankType": "BCTP000001",
			"isFourCheck": "1",
			"fourCheckResult": "1",
			},
		"familyInfo": {
			"homeArea": "山东省烟台市福山区八角口村011号",
			"localResident": "HRTP000001",
			"homeInfo": "HSST000010",
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
			"contactRel": "RELA000004",
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
		"frontAccountInfo":{

		},
		"fundSpecialInfo": {
			"referType": "04"
			},
		"idCardImageInfo": {
			 "idFrontImage": "http://10.139.60.163/group1/M01/60/18/Cos8o11cspSAFod8AACO72pQ8oY140.jpg",
			"idBackImage": "http://10.139.60.163/group1/M01/60/18/Cos8o11csmmAZzJFAAR33xq9DTI426.jpg",
			#"handUpImage": "http://10.139.60.163/group1/M01/60/18/Cos8o11csr-AFJEbAACXHvIDsGQ282.jpg",
			"livingBodyImage": "http://10.139.60.163/group1/M01/60/18/Cos8o11csr-AFJEbAACXHvIDsGQ282.jpg",
			"signPic": "http://10.139.60.163/group1/M01/60/1A/Cos8o11dF6qAKL-oAABi5feQHFE174.png",
			"signType": None
			},
		"frontControlInfo": {
			"noSettleFundCode": [],
			"maxAuditTimes":"10",
			#"controlFundCode":"FDCD000042",
			#"removedFundCodes":"FDCD000033"
			},
		}


	return yushenpi_data
#预审批筛选查询
guocheng_data = { "PreCheckGUID":"28e5e3b0245b486da9936668242d7376"}
#重放请求参数
chongfang_data = {
    "batchNo": "1",
    "routeAuthTokenList": [
        "a2c718ce23394ae184d1687ca8c9617a"
    ]}

