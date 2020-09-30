
data1 = {
    "name":"张三",
    "age":"24"
}
data2 = {
	"brNo": "2003",
	"batNo": "17442194-5017348263756781574",
	"dataCnt": "1",
	"list": [{
		"pactNo": "2003VDMtX1QxRTEzIzRGWV9FWSVMNiU=",
		"custName": "葛静柏",
		"idType": "0",
		"idNo": "341126197709218366",
		"idPreDate": "20000802",
		"idEndDate": "20200802",
		"custType": "02",
		"trade": "26",
		"sex": "2",
		"birth": "19770921",
		"marriage": "90",
		"children": "2",
		"edu": "60",
		"degree": "9",
		"telNo": "13552535506",
		"phoneNo": "13552535506",
		"postCode": "999999",
		"postAddr": "暂缺",
		"homeArea": "000000",
		"homeTel": None,
		"homeCode": "999999",
		"homeAddr": "住宅地址",
		"homeSts": "9",
		"income": "5000.0",
		"mateName": None,
		"mateIdtype": None,
		"mateIdno": None,
		"mateWork": None,
		"mateTel": None,
		"projNo": "7667548",
		"prdtNo": "200301",
		"pactAmt": "36000.00",
		"feeTotal": None,
		"premNo": None,
		"premRate": None,
		"lnRate": "2",
		"appArea": "341126",
		"appUse": "07",
		"termMon": "6",
		"termDay": "0",
		"vouType": "4",
		"endDate": "20200903",
		"payType": "01",
		"payDay": None,
		"vouAmt": None,
		"ifCar": "2",
		"ifCarCred": "2",
		"ifRoom": "2",
		"ifMort": "2",
		"ifCard": "2",
		"cardAmt": "0",
		"ifApp": "1",
		"ifId": "1",
		"ifPact": "1",
		"prePactNo": "10000000052487",
		"czPactNo": None,
		"workSts": None,
		"cardChn": None,
		"ifLaunder": "02",
		"sales": "01",
		"factPactNo": "KK181580019010000160",
		"ifAgent": "02",
		"country": "CHN",
		"homeIncome": "60000.0",
		"profession": "12",
		"creditNo": None,
		"creditLines": None,
		"creditBegDt": None,
		"creditEndDt": None,
		"creditSts": None,
		"creditPactNo": None,
		"workType": "Z",
		"workName": "暂缺",
		"workWay": "Z",
		"workCode": None,
		"workAddr": None,
		"workDuty": "4",
		"workTitle": "9",
		"workYear": None,
		"listAc": [{
			"acUse": "2",
			"acAmt": "36000.00",
			"acType": "11",
			"acno": "6222809876543210000",
			"acName": "葛静柏",
			"bankCode": "005",
			"bankProv": None,
			"bankCity": None,
			"bankSite": None,
			"idType": "0",
			"idNo": "341126197709218366",
			"phoneNo": "13552535506",
			"validDate": None,
			"cvvNo": None
		}, {
			"acUse": "1",
			"acAmt": None,
			"acType": "11",
			"acno": "6222809876543210000",
			"acName": "葛静柏",
			"bankCode": "005",
			"bankProv": None,
			"bankCity": None,
			"bankSite": None,
			"idType": "0",
			"idNo": "341126197709218366",
			"phoneNo": "13552535506",
			"validDate": None,
			"cvvNo": None
		}],
		"listCom": [],
		"listRel": [],
		"listGage": [],
		"Launder": "03"
	}]
}
data3 = []
print(len(data3) == 0 )


def json_to_list(data):
	for key,value in data.items():
		if isinstance(value,dict):
			json_to_list(value)
		elif isinstance(value,list):
			if len(value)!=0:
				for list_value in value:
					if isinstance(list_value,dict):
						json_to_list(list_value)
			else:
				field_name_list.append(key)
				field_value_list.append(None)
		else:
			field_name_list.append(key)
			field_value_list.append(value)
	return field_name_list,field_value_list
if __name__ == '__main__':
	field_name_list,field_value_list = json_to_list(data2)
	print(field_name_list)
	print(field_value_list)
