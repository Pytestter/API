from luyou_pre_approval_query import *
from luyou_pre_approval import *
from loan import *
while True:
    print("=" * 30 + "资方平台接口调用链" + "=" * 30)
    # 初始化接口实例化
    init_query = Init_Query()
    # 调用初始化接口
    res_init = init_query.test_ly_init_query(routeAuthToken=None)
    # 申请金额，申请期数，客户类型，客户标识
    pre_list = res_init + ('20000', '6', "66客户", "6")
    # 授信接口
    pre_approval = PreApproval(pre_list)
    res = pre_approval.test_pre_approval()
    # 授信查询接口
    if res['message'] == '成功':
        pre_res = init_query.test_ly_init_query(res_init[0])
        loan_list = pre_approval.test_pre_approval_result()
        if pre_res['data']['status'] == 'passed':
            loan = Loan(loan_list)
            loan.test_loan()
            loan.test_mongo_loan()


