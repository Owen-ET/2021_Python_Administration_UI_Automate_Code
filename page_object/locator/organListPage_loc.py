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
    # 查询机构单位
    seartOrgan_loc = (By.CSS_SELECTOR,".indexStyle>.el-input__inner")
    # 搜索按钮
    seartButton_loc = (By.CSS_SELECTOR,".el-form-item__content>.el-button--primary")
    # 机构复选框
    organCheckbox_loc = (By.CSS_SELECTOR,".el-table__row>td>div>label")
    # 删除机构按钮
    delOrganButton_loc = (By.CSS_SELECTOR,".tableHeader>div:nth-child(2)>span:nth-child(4)")
    # 删除确定按钮
    delSureButton_loc = (By.CSS_SELECTOR,".el-message-box__btns>.el-button--primary")
    # 删除成功提示
    delSuccess_loc = (By.CSS_SELECTOR,".el-message__content")