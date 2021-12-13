# This is a sample Python script.
import sys

from PyQt5.QtWidgets import *


from Home import Ui_MainWindow
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# pyinstaller -F -w -i Format.ico main.py
# 或
# pyinstaller -F -c -i Format.ico main.py
# (建议先用-c，这样如果打包不成功的话可以看到哪里有错）
# -F 指只生成一个exe文件，不生成其他dll文件
# -w 不弹出命令行窗口
# -i 设定程序图标 ，其后面的ico文件就是程序图标
# main.py 就是要打包的程序
# -c 生成的exe文件打开方式为控制台打开。


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    App = QApplication(sys.argv)    # 创建QApplication对象，作为GUI主程序入口
    aw = Ui_MainWindow()    # 创建主窗体对象，实例化Ui_MainWindow
    w = QMainWindow()      # 实例化QMainWindow类
    aw.setupUi(w)         # 主窗体对象调用setupUi方法，对QMainWindow对象进行设置
    aw.init()
    w.show()               # 显示主窗体
    # App.exit()
    sys.exit(App.exec_())   # 循环中等待退出程序


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
