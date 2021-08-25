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
from page_object.test_case.base_testcase import BaseTestCase


@allure.feature("执行下面的用例：")
class TestOrgan(BaseTestCase):


    @allure.story('测试用例：添加机构')
    def test_addOrgan(self):
        """添加机构"""
        self.organListPage.goto_newOrganPage().newOrgan()
        result = self.organListPage.seart_organ()
        assert result == "存在"

    # def test_upload(self):
    #     """上传文件"""
    #     self.login.goto_mainPage()\
    #         .goto_organListPage()\
    #         .upload()

    @allure.story('测试用例：删除机构')
    def test_deleteOrgan(self):
        """删除机构"""
        self.organListPage.delete_organ()
        successText = self.organListPage.delete_success()
        assert successText == "删除成功"