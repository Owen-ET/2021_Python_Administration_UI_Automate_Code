#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/21 16:45
# @Author  : zc
# @File    : newOrganPage_loc.py
from selenium.webdriver.common.by import By
from page_object.utils.functions import Functions as Fun


class NewOrganPageLoc:

    organData = Fun().getYamlData('organ')
    provinceLevelArea = organData['provinceLevelArea']
    municipalLevelArea = organData['municipalLevelArea']
    districtLevelArea = organData['districtLevelArea']
    districtName = organData['districtName']
    organType = organData['organType']
    organTypeName = organData['organTypeName']
    addressName = organData['addressName']
    fullAddress = organData['fullAddress']
    contacts = organData['contacts']
    telePhone = organData['telePhone']
    explain = organData['explain']

    organName = organData['organName']
    organCode = organData['organCode']
    fullAddressText = organData['fullAddressText']
    contactsText = organData['contactsText']
    telePhoneText = organData['telePhoneText']
    explainText = organData['explainText']



    # 机构名称
    organName_loc = (By.CSS_SELECTOR, ".formtable > form > div:nth-child(1) >div>div>div>input")
    # 机构编码
    organCode_loc = (By.CSS_SELECTOR, ".formtable > form > div:nth-child(2) >div>div>div>input")
    # 单位级别
    unitLevel_loc = (By.CSS_SELECTOR, ".formtable > form > div:nth-child(3) >div>div>div>div>input")
    # 选择单位级别：区级
    selectDistrictLevel_loc = (By.XPATH, "//body/div[2]/div/div/ul/li[2]")
    # 所属行政区：省级地区
    provinceLevelArea_loc = (By.XPATH, "//*[@placeholder='{}']".format(provinceLevelArea))
    # 行政区省级：天津
    TJProvince1_loc = (By.XPATH, "//body/div[3]/div/div/ul/li[2]")
    # 所属行政区：市级地区
    municipalLevelArea_loc = (By.XPATH, f"//*[@placeholder='{municipalLevelArea}']")
    # 行政区市级：天津市
    TJMunicipal1_loc = (By.XPATH, "//body/div[4]/div/div/ul/li[2]")
    # 所属行政区：区级地区
    districtLevelArea_loc = (By.XPATH, f"//*[@placeholder='{districtLevelArea}']")
    # 行政区区级：某某区
    TJDistrict1_loc = (By.XPATH, "//body/div[5]/div/div/ul/li["+ str(Fun().getIndex(f'{districtLevelArea}',f'{districtName}')) +"]")
    # 机构类型
    organType_loc = (By.XPATH, f"//*[@placeholder='{organType}']")
    # 选择机构类型
    selectOrganType_loc = (By.XPATH, "//body/div[6]/div/div/ul/li[" + str(Fun().getIndex(organType[3:], f'{organTypeName}')) + "]")
    # 机构地址：省
    provinceLevel_loc = (By.XPATH, "//*[@placeholder='" + provinceLevelArea[0] + "']")
    # 机构地址省级：天津市
    TJProvince2_loc = (By.XPATH, "//body/div[7]/div/div/ul/li[2]")
    # 机构地址：市
    municipalLevel_loc = (By.XPATH, "//*[@placeholder='"+municipalLevelArea[0]+"']")
    # 机构地址市级：天津市
    TJMunicipal2_loc = (By.XPATH, "//body/div[8]/div/div/ul/li[2]")
    # 机构地址：区
    districtLevel_loc = (By.XPATH, "//*[@placeholder='"+districtLevelArea[0]+"']")
    # 机构地址区级：某某区
    TJDistrict2_loc = (By.XPATH, "//body/div[9]/div/div/ul/li["+ str(Fun().getIndex(f'{districtLevelArea}',f'{addressName}')) +"]")
    # 详细地址
    fullAddress_loc = (By.XPATH, f"//*[@placeholder='{fullAddress}']")
    # 联系人
    contacts_loc = (By.XPATH, f"//*[@placeholder='{contacts}']")
    # 联系电话
    telePhone_loc = (By.XPATH, f"//*[@placeholder='{telePhone}']")
    # 说明
    explain_loc = (By.XPATH, f"//*[@placeholder='{explain}']")
    # 机构保存按钮
    saveButton_loc = (By.CSS_SELECTOR, ".el-button--primary")








if __name__ == '__main__':
    # print(OrganPage().provinceLevelArea[0])
    # test = '请选择机构类型'
    # print(test[3:])

    def testFun():
        temp = [lambda x: i * x for i in range(4)]
        return temp

        # return(lambda x: i * x for i in range(4))

        # for i in range(4):
        #     yield lambda x: i * x


    for everyLambda in testFun():
        print(everyLambda(2))