#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/21 10:03
# @Author  : zc
# @File    : test_organ.py
from page_object.page.web import Web


class TestOrgan:

    def setup(self):
        self.web = Web().startWeb()
        self.login = self.web.goto_loginPage()

    def teardown(self):
        # Web().stopWeb()
        self.web.stopWeb()

    def test_addOrgan(self):
        """添加机构"""
        self.login.goto_mainPage()\
            .goto_organListPage()\
            .goto_newOrganPage()\
            .newOrgan()

    def test_upload(self):
        """上传文件"""
        self.login.goto_mainPage()\
            .goto_organListPage()\
            .upload()