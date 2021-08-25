#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/05/12 14:56
# @Author  : zc
# @File    : organList_page.py
from selenium.webdriver.common.by import By

from page_object.locator.organListPage_loc import OrganListPageLoc as loc
from page_object.page.base_page import Page
from page_object.page.newOrgan_page import NewOrganPage
from page_object.utils.functions import Functions as Fun


class OrganListPage(Page):
    """机构信息列表页面"""

    organListData = Fun().getYamlData('organList')
    filePath = organListData['filePath']
    organData = Fun().getYamlData('organ')
    organName = organData['organName']

    def goto_newOrganPage(self):
        """跳转新增机构页面"""

        # 点击新增机构按钮
        self.el_click(loc.addOrganButton_loc)
        return NewOrganPage(self.driver)

    def upload(self):
        """上传文件"""
        self.el_click(loc.batchImportButton_loc)
        self.el_click(loc.uploadOfCheckButton_loc)
        Fun().upload_file(self.filePath)

    def delete_organ(self):
        """删除机构"""

        # 点击删除按钮
        self.el_sendKeys(loc.seartOrgan_loc,self.organName)
        self.el_click(loc.seartButton_loc)
        self.el_click(loc.organCheckbox_loc)
        self.el_click(loc.delOrganButton_loc)
        self.el_click(loc.delSureButton_loc)

    def delete_success(self):
        """删除成功提示"""
        return self.get_text(loc.delSuccess_loc)

    def seart_organ(self):
        """查询数据"""
        self.el_sendKeys(loc.seartOrgan_loc, self.organName)
        self.el_click(loc.seartButton_loc)
        try:
            self.webDriverWait(loc.organCheckbox_loc)
            return "存在"
        except:
            return "不存在"