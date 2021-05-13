#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/21 14:41
# @Author  : zc
# @File    : loginPage_loc.py
from selenium.webdriver.common.by import By


class LoginPageLoc:

    # 用户名
    telephone_loc = (By.NAME, "telephone")
    # 密码
    password_loc = (By.NAME, "password")
    # 登录按钮
    loginButton_loc = (By.CSS_SELECTOR, ".el-button--medium")