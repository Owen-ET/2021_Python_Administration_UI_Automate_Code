#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/21 15:40
# @Author  : zc
# @File    : mainPage_loc.py
from selenium.webdriver.common.by import By


class MainMenuLoc:

    """左侧菜单"""
    # 1、订单管理
    # 2、台账申报管理


    # 3、基础信息维护
    baseInfo_loc = (By.XPATH, "//ul/div[4]")
    # 机构信息管理
    organInfo_loc = (By.XPATH, "//ul/div[4]/li/ul/div")

    # 4、系统管理

