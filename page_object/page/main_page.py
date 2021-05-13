#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/20 09:31
# @Author  : zc
# @File    : main_page.py
from page_object.page.base_page import Page
from page_object.page.organList_page import OrganListPage
from page_object.locator.mainPage_loc import MainMenuLoc as loc



class MainPage(Page):
    """首页"""

    def goto_organListPage(self):
        """跳转机构信息列表页面"""
        self.el_click(loc.baseInfo_loc)
        self.el_click(loc.organInfo_loc)
        return OrganListPage(self.driver)


