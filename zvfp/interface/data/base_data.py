'''
titile : 存放基础数据
author:张来明
date:20191023
version:python3.6.5
'''
import time
data = str(int(time.time()))
import re
#请求头信息
headers = {
    "Content-Type":"application/json",
    "apiToken":"e6475549-4681-4b12-9ca0-d28c0e03230a",
    "sync":"false",
    "X-CLIENT-ID":"123"
        }

vbs_headers = {
    "apiToken":"b96f53c7-0442-4db8-ac96-eaaafd1cef54",
    "nonce":"123456789456",
    "timestamp":"1561947713345",
    "signature":"NWJhM2UzNWM1ODUzNjc2MmYxOTRiNjM2N2E2ZThjMGU=",
}
def bank_information(bank_name='建设银行',bank_card='6217008485838356417'):
    bank_infomation = {
        "bank_no":bank_code()[bank_name],
        "bank_card_no":bank_card,
        "bank_name":bank_name,
        "repay_bank_no":bank_code()[bank_name],
        "repay_bank_card_no":bank_card,
        "repay_bank_name":bank_name
    }
    return bank_infomation

#所有的url地址：
init_url = 'http://api-gateway-t2.dev.vcredit.com.local/fund/initialize'  #初始化请求地址
open_url = 'http://api-gateway-t2.dev.vcredit.com.local/fund/account/open' #开户地址
open_query_url = 'http://api-gateway-t2.dev.vcredit.com.local/fund/account/result/5d0b74419ac7f6001bb4bc7f' #开户查询地址 {commandId}
luyou_init_url = 'http://api-gateway-t2.dev.vcredit.com.local/fund/integratedQuery/'  #资方路由初始化/资方路由查询
luyou_url2 = 'http://api-gateway-t2.dev.vcredit.com.local/route/command'  #资方路由2.0初始化接口
luyou_select_url = 'http://api-gateway-t2.dev.vcredit.com.local/fund/routeScreen'  #资方路由预筛选
select_query_url = 'http://api-gateway-t2.dev.vcredit.com.local/fund/routeScreenQuery' #资方路由预筛选查询
luyou_pre_url = 'http://api-gateway-t2.dev.vcredit.com.local/fund/routeDataSubmit' #资方路由预审批
document_upload_url = 'http://api-gateway-t2.dev.vcredit.com.local/fund/document/upload/'  #文件上传
ducument_obtain_url = 'http://api-gateway-t2.dev.vcredit.com.local/fund/document/obtain'   #文件下载
ducument_obtain_query_url = 'http://api-gateway-t2.dev.vcredit.com.local/fund/document/obtain/'  #文件下载查询
loan_url = 'http://api-gateway-t2.dev.vcredit.com.local/payment/loan' #放款
loan_query_url = 'http://api-gateway-t2.dev.vcredit.com.local/payment/instruction?' #放款查询
loan_cancel_url = 'http://api-gateway-t2.dev.vcredit.com.local/fund/loan/cancel'  #放款取消
loan_query_cancel_url = 'http://api-gateway-t2.dev.vcredit.com.local/fund/loan/cancel/result/' #放款查询
repay_plan_query_url = 'http://api-gateway-uat.msa.vcredit.com.local:8000/fund/repay-schedule'  #还款计划查询
loan_reconcialation_uat_url = 'http://10.10.24.106:30900/reconciliation'  #放款对账uat
loan_reconcialation_sit2_url = 'http://10.138.62.22:30900//reconciliation'  #放款对账sit2
yue_query_url_url = 'http://api-gateway-t3.dev.vcredit.com.local/fund/balance-info-query' #余额查询
bank_update_url = 'http://api-gateway-t2.dev.vcredit.com.local/fund/bank-update'  #更换银行卡
bank_query_update_url = 'http://api-gateway-t2.dev.vcredit.com.local/fund/bank/update' #更换银行卡查询
calculate_url = 'http://api-gateway-t2.dev.vcredit.com.local/fund/repay-calculate'  #还款试算
deduct_url = 'http://api-gateway-t2.dev.vcredit.com.local/fund/deduct'   #扣款
deduct_query_url = 'http://api-gateway-t2.dev.vcredit.com.local/fund/deduct?'  #扣款查询
repay_info_url = 'http://api-gateway-t2.dev.vcredit.com.local/fund/repay-info' #还款推送
guarantee_url = 'http://api-gateway-t2.dev.vcredit.com.local/fund/guarantee/payment'
fund_info_url = 'http://10.138.60.136:18002/vcl/vcl-service/fundInfo/1'
vbs_sign_url = 'http://api-gateway-t2.dev.vcredit.com.local/entrust/apply'  #签约
vbs_sign_verigy_url = 'http://api-gateway-t2.dev.vcredit.com.local/entrust/verify' #签约确认
vbs_sign_query = 'http://api-gateway-t2.dev.vcredit.com.local/entrust/apply/'  #签约查询
pre_check_url = 'http://api-gateway-t2.dev.vcredit.com.local/fund/platform/preCheck' #撞库
query_agreement_url = 'http://api-gateway-t2.dev.vcredit.com.local/fund/platform/queryAgreement'
pre_apply_url = 'http://api-gateway-t2.dev.vcredit.com.local/fund/platform/preApply' #授信申请


