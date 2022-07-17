# Go File 启动器

## 打包流程
```bash
pip install pyqt5 pyinstaller requests
pyuic5 -o ui.py main.ui
pyinstaller  --noconsole -F ./main.py --icon icon.png
```
