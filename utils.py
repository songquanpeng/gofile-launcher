import os
import socket
import sys

import requests


def get_ips():
    return socket.gethostbyname_ex(socket.gethostname())[2]


def system_related_secret():
    return socket.gethostname() + os.getcwd() + str(get_ips()) + str(os.path.getctime(sys.argv[0]))


def get_latest_version(repository, username="songquanpeng"):
    try:
        data = requests.get(f"https://api.github.com/repos/{username}/{repository}/releases/latest").json()
    except:
        return None
    latest_version = data["tag_name"]
    return latest_version
