from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
import requests
from ui import Ui_MainWindow
from threading import Thread
import subprocess
import sys
import os


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.gofile = None

    @pyqtSlot()
    def on_startBtn_clicked(self):
        if self.gofile is None:
            if os.path.exists("go-file.exe"):
                port = self.portSpinBox.text()
                host = self.hostLineEdit.text()
                path = self.pathLineEdit.text()
                self.gofile = subprocess.Popen(["go-file.exe", "--port", f"{port}", "--host", f"{host}", "--path", f"{path}"], shell=True)
                self.statusbar.showMessage("服务已启动")
                self.startBtn.setText("终止")
            else:
                QMessageBox.information(self, "未能找到 go-file.exe", "请点击更新按钮进行下载或者手动下载后放到本启动器相同目录下", QMessageBox.Ok)
        else:
            if os.name == "nt":
                subprocess.Popen("TASKKILL /F /PID {pid} /T".format(pid=self.gofile.pid))
            else:
                # Not tested.
                # https://stackoverflow.com/questions/4789837/how-to-terminate-a-python-subprocess-launched-with-shell-true
                self.gofile.kill()
            self.gofile = None
            self.statusbar.showMessage("服务已终止")
            self.startBtn.setText("启动")

    @pyqtSlot()
    def on_chooseBtn_clicked(self):
        path = QFileDialog.getExistingDirectory(self, "选择要分享的目录", ".")
        self.pathLineEdit.setText(path)
        self.statusbar.showMessage(f"选择：{path}")

    @pyqtSlot()
    def on_updateBtn_clicked(self):
        worker = ThreadDownloader(self.statusbar, self.updateBtn)
        worker.start()


class ThreadDownloader(Thread):
    def __init__(self, statusbar, updateBtn):
        super().__init__()
        self.statusbar = statusbar
        self.updateBtn = updateBtn

    def run(self):
        self.updateBtn.setEnabled(False)
        self.statusbar.showMessage("正在从 GitHub 上获取最新版 ...")
        res = requests.get("https://github.com/songquanpeng/go-file/releases/latest/download/go-file.exe")
        if res.status_code != 200:
            self.statusbar.showMessage(f"下载失败：{res.text}")
        else:
            with open("go-file.exe", "wb") as f:
                f.write(res.content)
            self.statusbar.showMessage(f"下载完成")
        self.updateBtn.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Dialog = MainWindow()
    Dialog.show()
    sys.exit(app.exec_())
