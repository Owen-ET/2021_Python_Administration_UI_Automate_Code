#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/21 10:03
# @Author  : zc
# @File    : test_organ.py
import os

import allure
from selenium import webdriver
from page_object.page.web import Web
from selenium.webdriver.chrome.options import Options

@allure.feature("执行下面的用例：")
class TestOrgan:

    def setup(self):

        self.web = Web().startWeb()
        self.login = self.web.goto_loginPage()

    def teardown(self):
        # Web().stopWeb()
        self.web.stopWeb()

    @allure.story('测试用例：添加机构')
    def test_addOrgan(self):
        """添加机构"""
        self.login.goto_mainPage()\
            .goto_organListPage()\
            .goto_newOrganPage()\
            .newOrgan()

    # def test_upload(self):
    #     """上传文件"""
    #     self.login.goto_mainPage()\
    #         .goto_organListPage()\
    #         .upload()

    @allure.story('测试用例：删除机构')
    def test_deleteOrgan(self):
        """删除机构"""
        self.organListPage = self.login.goto_mainPage().goto_organListPage()
        self.organListPage.delete_organ()
        successText = self.organListPage.delete_success()
        assert successText == "删除成功"