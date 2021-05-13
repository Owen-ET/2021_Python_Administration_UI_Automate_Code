#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/05/12 14:49
# @Author  : zc
# @File    : organListPage_loc.py
from selenium.webdriver.common.by import By


class OrganListPageLoc:


    # 新增机构按钮
    addOrganButton_loc = (By.CSS_SELECTOR, ".tableHeader > div:nth-child(2) > span:nth-child(1)")
    # 机构导入按钮
    batchImportButton_loc = (By.CSS_SELECTOR, ".tableHeader > div:nth-child(2) > span:nth-child(2)")
    # 上传并校验按钮
    uploadOfCheckButton_loc = (By.CSS_SELECTOR, ".el-upload")
