#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/21 14:56
# @Author  : zc
# @File    : functions.py
import os
# import time
# import pyperclip
import yaml
# from pykeyboard import PyKeyboard
# from pymouse import PyMouse


class Functions:

    def upPath(self):
        """获取上级路径"""
        path = os.path.dirname(os.path.dirname(__file__))
        return path

    def getData(self, path):
        """获取yaml数据"""
        with open(path, 'r', encoding='utf-8') as file:
            data = yaml.load(file)
            return data

    def getYamlPath(self):
        """获取公共不同yaml路径"""
        path = self.upPath() + '/data/common.yaml'
        return self.getData(path)

    def getYamlData(self, yamlName):
        """获取当前yaml数据"""
        path = self.upPath() + self.getYamlPath()[yamlName]
        return self.getData(path)

    def getIndex(self,type,name):
        """获取区级对应角标index"""
        list = self.getYamlData('selectData')[type]
        for index,value in enumerate(list):
            if name in value:
                return index+1

    def upload_file(self, path):
        """PyUserInput方法"""
        pass


        # # 创建鼠标对象
        # k = PyKeyboard()
        # # 创建键盘对象
        # m = PyMouse()
        # filepath = "/"
        # # 模拟快捷键Command+Shift+G
        # k.press_keys(["Command", "Shift", "G"])
        # # 输入文件路径
        # x_dim, y_dim = m.screen_size()
        # m.click(x_dim // 2, y_dim // 2, 1)
        # # 复制文件路径开头的斜杠/
        # pyperclip.copy(filepath)
        # # 粘贴斜杠/
        # k.press_keys(["Command", "V"])
        # time.sleep(2)
        # # 输入文件全路径进去
        # k.type_string(path)
        # fileName = '机构信息-批量导入模板 (9).xls'
        # pyperclip.copy(fileName)
        # k.press_keys(["Command", "V"])
        # time.sleep(2)
        # k.press_key("Return")
        # time.sleep(2)
        # k.press_key("Return")
        # time.sleep(2)

    # def upload_file2(self,path):
    #     """pyautogui方法"""
    #     filepath = "/"
    #     pyautogui.press('shiftleft')
    #     pyautogui.hotkey("Command", "Shift", "G")
    #     pyautogui.typewrite(path, interval=0.25)
    #     pyautogui.press('return')
    #     time.sleep(2)
    #     pyautogui.press('return')
    #     time.sleep(2)