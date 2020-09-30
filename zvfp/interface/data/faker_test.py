'''
Faker 造数模块：

'''


from faker import Faker

faker = Faker('zh_CN')  # 显示语言，默认英文


print("name:",faker.name())  # 姓名
print("address:", faker.address())  # 地址和邮编
print("postcode:",faker.postcode())  # 邮编
# print("text:",faker.text())

print("country:",faker.country())  # 国家名称
print("country_code:",faker.country_code())  # 国家英文简称

print("province:",faker.province())  # 省名称
print("city_name:",faker.city_name())  # 城市名称
print("city:",faker.city())  # 县名
print("district:",faker.district())  # 区

print("street_address:",faker.street_address())  # 街道地址
print("street_name:",faker.street_name())  # 街道名称



print("building_number:",faker.building_number())  # 大厦编号

# 公司相关
print("company:",faker.company())  # 公司名称

# 信用卡
print("credit_card_full:",faker.credit_card_full(card_type=None))  # 完整信用卡信息
print("credit_card_expire:",faker.credit_card_expire(start="now", end="+10y",date_format="%m/%y"))  # 信用卡有效期
print("credit_card_provider:",faker.credit_card_provider(card_type=None))  # 发卡机构
print("credit_card_number:",faker.credit_card_number(card_type=None))  # 卡号
print("credit_card_security_code:",faker.credit_card_security_code(card_type=None))  # 安全码






