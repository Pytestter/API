from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
#创建浏览器对象
class PageObject:
    def __init__(self,url):
        #创建一个浏览器对象
        self.browser = webdriver.Chrome()
        #初始化地址
        self.url = url
    def get_page_content(self):
        '''输入查询内容，并单击【查询】按钮'''
        try:
            self.browser.get(self.url)
            #窗口最大化
            self.browser.maximize_window()
            #直到对应的title出现才继续往下走
            WebDriverWait(self.browser,20).until(EC.title_contains("Discover"))
            #点击时间下拉选择框
            self.browser.find_element_by_css_selector(".euiIcon.euiIcon--medium.euiButtonEmpty__icon").click()
            #通过标签属性定位"today"元素，并选择点击
            self.browser.find_element_by_css_selector('button[data-test-subj="superDatePickerCommonlyUsed_Today"]').click()
            #WebDriverWait(self.browser, 20).until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR,'.euiFieldText')))
            #点击【搜索输入框】,获取焦点
            self.browser.find_element_by_xpath(".//div[@class='kuiLocalSearchAssistedInput']/div/div/input").click()
            #输入输入查找的条件token值
            self.browser.find_element_by_xpath(".//div[@class='kuiLocalSearchAssistedInput']/div/div/input").send_keys("1afbdcbf1a294fed905f77455bb301c8")
            #点击【查询】按钮
            self.browser.find_element_by_xpath(".//span[@class='euiButton__text euiSuperUpdateButton__text']").click()
            time.sleep(2)
            #点击时间正序排列
            self.browser.find_element_by_id("docTableHeaderFieldSort@timestamp").click()
            #点击第一个展开
            content=self.browser.find_element_by_xpath(".//tr[@ng-repeat='field in fields'and data-test-subj='tableDocViewRow-trace']/td[3]/div/span").text
            print(content)
        finally:
            #self.browser.close()
            pass

p = PageObject(url='http://10.138.61.94:5601/app/kibana#/discover?_g=()')
p.get_page_content()