<p align="center">
  <a href="https://github.com/songquanpeng/gofile-launcher"><img src="./icon.png" width="200" height="200" alt="gofile-launcher"></a>
</p>

<div align="center">

# Go File 启动器
_✨ 为 Go File 制作的启动器，方便不想或不会使用终端的用户 ✨_  

</div>

<p align="center">
  <a href="https://raw.githubusercontent.com/songquanpeng/gofile-launcher/master/LICENSE">
    <img src="https://img.shields.io/github/license/songquanpeng/gofile-launcher?color=brightgreen" alt="license">
  </a>
  <a href="https://github.com/songquanpeng/gofile-launcher/releases/latest">
    <img src="https://img.shields.io/github/v/release/songquanpeng/gofile-launcher?color=brightgreen&include_prereleases" alt="release">
  </a>
  <a href="https://github.com/songquanpeng/gofile-launcher/releases/latest">
    <img src="https://img.shields.io/github/downloads/songquanpeng/gofile-launcher/total?color=brightgreen&include_prereleases" alt="release">
  </a>
</p>

<p align="center">
  <a href="https://github.com/songquanpeng/gofile-launcher/releases">Go File 下载</a>
  ·
  <a href="https://github.com/songquanpeng/gofile-lancher/releases/latest">启动器下载</a>
</p>

## 截图展示
![demo.png](demo.png)


## 打包流程
```bash
pip install pyqt5 pyinstaller requests
pyuic5 -o ui.py main.ui
pyinstaller --noconsole -F ./main.py --icon icon.png -n gofile-launcher.exe
```
