#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/20 09:23
# @Author  : zc
# @File    : base_page.py
from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, loc):
        """查找单元素"""
        return self.driver.find_element(*loc)

    def find_elements(self, loc):
        """查找多元素"""
        return self.driver.find_elements(*loc)

    def el_click(self, loc):
        """点击事件"""
        self.webDriverWait(loc).click()

    def el_sendKeys(self, loc, value):
        """输入事件"""
        self.webDriverWait(loc).send_keys(value)

    def webDriverWait(self,loc):
        """显式等待，查找元素"""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
        sleep(0.3)
        return self.find_element(loc)

    def get_text(self,loc):
        """获取元素的内容"""
        return self.webDriverWait(loc).text