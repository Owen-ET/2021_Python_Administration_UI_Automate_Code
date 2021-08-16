#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/20 09:21
# @Author  : zc
# @File    : web.py

import os
from selenium import webdriver
from page_object.page.login_page import LoginPage
from selenium.webdriver.chrome.options import Options
from page_object.utils.functions import Functions as Fun


class Web:

    def startWeb(self):
        """开启WEB自动化"""

        # 控制是否采用无界面形式运行自动化测试
        try:
            using_headless = os.environ["using_headless"]
        except KeyError:
            using_headless = None
            print('没有配置环境变量 using_headless, 按照有界面方式运行自动化测试')

        chrome_options = Options()
        if using_headless is not None and using_headless.lower() == 'true':
            print('使用无界面方式运行')
            chrome_options.add_argument("--headless")

        chromedriverPath = Fun().chromedriverPath()
        print(chromedriverPath)
        self.driver = webdriver.Chrome(executable_path=chromedriverPath,
                                       options=chrome_options)

        # self.driver = webdriver.Chrome("/Users/zhangc/Desktop/SQM_Project/内网Git代码仓库/github/Administration_UI_Automate_Code/page_object/utils/chromedriver")
        self.driver.get("https://recycle_dev.17mine.cn:9700/#/login")
        self.driver.implicitly_wait(10)
        return self

    def stopWeb(self):
        """关闭浏览器"""
        self.driver.quit()

    def goto_loginPage(self):
        """跳转登录页"""
        return LoginPage(self.driver)