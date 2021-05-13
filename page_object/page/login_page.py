#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/20 09:19
# @Author  : zc
# @File    : login_page.py
from selenium.webdriver.common.by import By
from page_object.locator.loginPage_loc import LoginPageLoc as loc
from page_object.page.base_page import Page
from page_object.page.main_page import MainPage
from page_object.utils.functions import Functions as Fun


class LoginPage(Page):
    """登录页"""

    loginData = Fun().getYamlData("login")

    def login_action(self):
        """登录操作"""
        self.el_sendKeys(loc.telephone_loc, self.loginData['telephone'])
        self.el_sendKeys(loc.password_loc, self.loginData['password'])
        self.el_click(loc.loginButton_loc)

    def goto_mainPage(self):
        """跳转首页"""
        self.login_action()
        return MainPage(self.driver)