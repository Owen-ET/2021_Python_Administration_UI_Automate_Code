#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/20 10:16
# @Author  : zc
# @File    : test.py

import unittest
from time import sleep

import yaml
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test:

    def setup(self):
        self.driver = webdriver.Chrome("/Users/zhangc/Desktop/SQM_Project/内网Git代码仓库/Administration_UI_Automate_Code/page_object/utils/chromedriver")
        self.driver.get("https://recycle_dev.17mine.cn:9700/#/login")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()


    def teardown(self):
        self.driver.quit()
        # pass


    def getDistrict(self,selects,name):
        list = self.getYamlData()[selects]
        for index,value in enumerate(list):
            if name in value:
                return index+1

    def getYamlData(self):
        with open('/Users/zhangc/Desktop/SQM_Project/内网Git代码仓库/Administration_UI_Automate_Code/page_object/data/selectData.yaml','r',encoding='utf-8') as file:
            data = yaml.load(file)
            return data


    def webDriverWait(self,loc):
        WebDriverWait(self.driver,1).until(EC.visibility_of_element_located((By.XPATH, loc)))
        sleep(0.3)
        return self.driver.find_element(By.XPATH, loc)


    def getfun(self):
        provincial = '省级地区'
        print(type(provincial[0]))






    def test1(self):
        provincial = '省级地区'
        municipal = '市级地区'
        district = '区级地区'
        self.driver.find_element(By.NAME, "telephone").send_keys("13642040631")
        self.driver.find_element(By.NAME, "password").send_keys("123456")
        self.driver.find_element(By.CSS_SELECTOR, ".el-button--medium").click()
        self.driver.find_element(By.XPATH, "//ul/div[4]").click()
        self.driver.find_element(By.XPATH, "//ul/div[4]/li/ul/div").click()
        self.driver.find_element(By.CSS_SELECTOR, ".tableHeader > div:nth-child(2) > span:nth-child(1)").click()
        # 修改
        self.driver.find_element(By.CSS_SELECTOR, ".formtable > form > div:nth-child(1) >div>div>div>input").send_keys("机构43006")
        self.driver.find_element(By.CSS_SELECTOR, ".formtable > form > div:nth-child(2) >div>div>div>input").send_keys("jg43006")
        self.driver.find_element(By.CSS_SELECTOR, ".formtable > form > div:nth-child(3) >div>div>div>div>input").click()
        self.webDriverWait("//body/div[2]/div/div/ul/li[2]").click()
        self.driver.find_element(By.XPATH, "//*[@placeholder='{}']".format(provincial)).click()
        self.webDriverWait("//body/div[3]/div/div/ul/li[2]").click()
        self.driver.find_element(By.XPATH, f"//*[@placeholder= '{municipal}']").click()
        self.webDriverWait("//body/div[4]/div/div/ul/li[2]").click()
        self.driver.find_element(By.XPATH, f"//*[@placeholder= '{district}']").click()
        self.webDriverWait("//body/div[5]/div/div/ul/li["+ str(self.getDistrict(f'{district}','滨海新区')) +"]").click()
        self.webDriverWait("//*[@placeholder='请选择机构类型']").click()
        self.webDriverWait("//body/div[6]/div/div/ul/li["+ str(self.getDistrict('机构类型','其他')) +"]").click()
        self.driver.find_element(By.XPATH, "//*[@placeholder='"+provincial[0]+"']").click()
        self.webDriverWait("//body/div[7]/div/div/ul/li[2]").click()
        self.driver.find_element(By.XPATH, "//*[@placeholder='"+municipal[0]+"']").click()
        self.webDriverWait("//body/div[8]/div/div/ul/li[2]").click()
        self.driver.find_element(By.XPATH, "//*[@placeholder='"+district[0]+"']").click()
        self.webDriverWait("//body/div[9]/div/div/ul/li["+ str(self.getDistrict(f'{district}','蓟州区')) +"]").click()
        self.webDriverWait("//*[@placeholder='请输入详细地址']").send_keys("蓟州区黄崖关")
        self.webDriverWait("//*[@placeholder='请输入联系人']").send_keys("zc联系人")
        self.webDriverWait("//*[@placeholder='请您输入手机号']").send_keys("13642040631")
        self.webDriverWait("//*[@placeholder='请输入说明 (100字以内)']").send_keys("zc机构说明")
        self.driver.find_element(By.CSS_SELECTOR, ".el-button--primary").click()
        sleep(0.5)
        # try:
        #     po = self.driver.find_element(By.CSS_SELECTOR, ".el-message__content").text
        #     assert po == "重复的机构编码","提示信息不对"
        # except Exception as e:
        #     print("打印："+ e)








if __name__ == '__main__':
    # Test().getDistrict(name='滨海新区')
    Test().getfun()