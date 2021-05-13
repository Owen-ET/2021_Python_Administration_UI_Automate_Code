#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/20 09:36
# @Author  : zc
# @File    : newOrgan_page.py
from page_object.page.base_page import Page
from page_object.locator.newOrganPage_loc import NewOrganPageLoc as loc


class NewOrganPage(Page):
    """新增机构页面"""

    def newOrgan(self):
        """新增机构"""

        # 输入机构名称
        self.el_sendKeys(loc.organName_loc, loc.organName)
        # 输入机构编码
        self.el_sendKeys(loc.organCode_loc, loc.organCode)
        # 点击单位级别下拉框，选择单位级别"区级"
        self.el_click(loc.unitLevel_loc)
        self.webDriverWait(loc.selectDistrictLevel_loc).click()
        # 点击所属行政区：省级地区并选择天津
        self.el_click(loc.provinceLevelArea_loc)
        self.webDriverWait(loc.TJProvince1_loc).click()
        # 点击所属行政区：市级地区并选择天津市
        self.el_click(loc.municipalLevelArea_loc)
        self.webDriverWait(loc.TJMunicipal1_loc)
        # 点击所属行政区：区级地区并选择某某区
        self.el_click(loc.districtLevelArea_loc)
        self.webDriverWait(loc.TJDistrict1_loc).click()
        # 点击机构类型并选择"其他"
        self.webDriverWait(loc.organType_loc).click()
        self.webDriverWait(loc.selectOrganType_loc).click()
        # 点击并输入机构地址：省
        self.el_click(loc.provinceLevel_loc)
        self.webDriverWait(loc.TJProvince2_loc).click()
        # 点击并输入机构地址：市
        self.el_click(loc.municipalLevel_loc)
        self.webDriverWait(loc.TJMunicipal2_loc).click()
        # 点击并输入机构地址：区
        self.el_click(loc.districtLevel_loc)
        self.webDriverWait(loc.TJDistrict2_loc).click()
        # 输入详细地址
        self.webDriverWait(loc.fullAddress_loc).send_keys(loc.fullAddressText)
        # 请输入联系人
        self.webDriverWait(loc.contacts_loc).send_keys(loc.contactsText)
        # 请输入联系电话
        self.webDriverWait(loc.telePhone_loc).send_keys(loc.telePhoneText)
        # 请输入说明
        self.webDriverWait(loc.explain_loc).send_keys(loc.explainText)
        # 点击保存按钮
        self.el_click(loc.saveButton_loc)