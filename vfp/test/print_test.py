from faker import Faker
faker = Faker('zh_CN')
id_number= faker.ssn(min_age=22, max_age=49)
