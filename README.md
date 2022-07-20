# Go File 启动器
> 为 [Go File](https://github.com/songquanpeng/go-file) 制作的启动器，方便不想或不会使用终端的用户

<p>
  <a href="https://raw.githubusercontent.com/songquanpeng/gofile-launcher/main/LICENSE">
    <img src="https://img.shields.io/github/license/songquanpeng/gofile-launcher?color=brightgreen" alt="license">
  </a>
  <a href="https://github.com/songquanpeng/gofile-launcher/releases/latest">
    <img src="https://img.shields.io/github/v/release/songquanpeng/gofile-launcher?color=brightgreen&include_prereleases" alt="release">
  </a>
  <a href="https://github.com/songquanpeng/gofile-launcher/releases/latest">
    <img src="https://img.shields.io/github/downloads/songquanpeng/gofile-launcher/total?color=brightgreen&include_prereleases" alt="release">
  </a>
</p>

请前往 [Release 页面](https://github.com/songquanpeng/gofile-lancher/releases/latest)下载最新版本。


## 截图展示
![demo.png](demo.png)
![demo_mac.png](demo_mac.png)

## 使用
**Windows**  
直接双击 gofile-launcher.exe 运行  
**macOS**  
```
chmod u+x gofile-launcher-macos # grant program executable privileges
```
之后直接双击运行 gofile-launcher-macos 或在终端中运行都可  
## 打包流程
```bash
pip install -r requirements.txt
pyuic5 -o ui.py main.ui
pyinstaller --noconsole -F ./main.py --icon icon.png -n gofile-launcher.exe # gofile-launcher on other platforms
```
