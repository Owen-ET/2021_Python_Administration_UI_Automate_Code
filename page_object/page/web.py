#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/20 09:21
# @Author  : zc
# @File    : web.py
from selenium import webdriver

from page_object.page.login_page import LoginPage


class Web:

    def startWeb(self):
        """开启WEB自动化"""
        self.driver = webdriver.Chrome("/Users/zhangc/Desktop/SQM_Project/内网Git代码仓库/Administration_UI_Automate_Code/page_object/utils/chromedriver")
        self.driver.get("https://recycle_dev.17mine.cn:9700/#/login")
        self.driver.implicitly_wait(10)
        return self

    def stopWeb(self):
        """关闭浏览器"""
        self.driver.quit()

    def goto_loginPage(self):
        """跳转登录页"""
        return LoginPage(self.driver)