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