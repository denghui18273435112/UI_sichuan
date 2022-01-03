import os
import time
import win32gui

import win32con

from config.Conf import get_file_path


def upload_files(filePath, browser_type="chrome"):
        '''
        上传文件的方法
        通过pywin32模块实现文件上传的操作
        :param filePath: 文件的绝对路径
        :param browser_type: 浏览器类型（默认值为chrome）
        :return:
        '''
        if browser_type.lower() == "chrome":
            title = "打开"
        elif browser_type.lower() == "firefox":
            title = "文件上传"
        elif browser_type.lower() == "ie":
            title = "选择要加载的文件"
        else:
            title = ""
        dialog = win32gui.FindWindow("#32770", title)
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级
        comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)   # 三级
        edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)  # 四级
        button = win32gui.FindWindowEx(dialog, 0, 'Button', "打开(&O)")  # 二级
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, get_file_path()+os.sep+filePath)  # 发送文件路径
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮
        time.sleep(3)
