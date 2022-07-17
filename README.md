# Go File 启动器
> 请前往 [Release 页面](https://github.com/songquanpeng/gofile-lancher/releases/latest)下载最新版启动器。

## 截图展示
![demo.png](demo.png)


## 打包流程
```bash
pip install pyqt5 pyinstaller requests
pyuic5 -o ui.py main.ui
pyinstaller --noconsole -F ./main.py --icon icon.png -n gofile-launcher.exe
```
