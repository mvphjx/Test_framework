from threading import Thread

import time
import win32con
import win32gui


class tpimgUload:
    def __init__(self, path):
        self.path = path

    def async(f):
        def wrapper(*args, **kwargs):
            thr = Thread(target=f, args=args, kwargs=kwargs)
            thr.start()

        return wrapper

    @async
    def operation_dialog(self):
        # 操作系统文件上传
        time.sleep(3)
        # win32gui
        dialog = win32gui.FindWindow('#32770', '打开')  # 对话框
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
        ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
        button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
        win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, self.path)  # 往输入框输入绝对地址
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button


if __name__ == '__main__':
    tpimgUload("test").operation_dialog()
