#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/08/25 17:13
# @Author  : zc
# @File    : base_testcase.py


from page_object.page.web import Web
from page_object.utils.functions import Functions as Fun


class BaseTestCase:

    loginData = Fun().getYamlData("login")

    def setup(self):
        self.web = Web().startWeb(self.loginData['url'])
        self.login = self.web.goto_loginPage()
        self.organListPage = self.login.goto_mainPage().goto_organListPage()

    def teardown(self):
        # Web().stopWeb()
        self.web.stopWeb()