import io
import os
import re
import sys
import zipfile
from time import sleep

import requests

# 这次的是第二版，修复了第一版的部分问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
url_update = r"http://leagueskin.net/p/download-mod-skin-2020-chn"
url_download = ""
save_file = "D://LOLskin_my"
url_edition = ""
file_edition = ""
1

def gethtml():
    global url_edition
    global url_download
    try:
        response = requests.get(url_update, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.66"})
        response.encoding = "utf-8"
        html = response.text
        # print(html)
        temp = re.findall("http://s4.modskinlolvn.com/MODSKIN_(.*?).zip",
                          html)  # http://s4.modskinlolvn.com/MODSKIN_11.13.3.zip
        url_download = "http://s4.modskinlolvn.com/MODSKIN_" + temp[0] + ".zip"
        url_edition = temp[0]
        url_edition = url_edition
    except Exception as e:
        print(e)
        print("get error!")


def geteditionNow():
    global file_edition
    try:
        if os.path.exists(save_file):
            pass
        else:
            os.mkdir(save_file)
        temp = []
        pathDir = os.listdir(save_file)
        for each in pathDir:
            temp = re.findall("LOLPRO (.*?).exe", each)
            if len(temp):
                break
        if len(temp):
            file_edition = temp[0]
        # else:
        #     file_edition   # 空列表
        # file_edition = file_edition
    except Exception as e:
        print(e)
    pass


def exe_download():
    try:
        pathDir = os.listdir(save_file)
        for each in pathDir:
            os.remove(save_file + "/" + each)
        print("delete old file!")
        file_name = save_file + "/download.zip"
        down_res = requests.get(url_download)
        with open(file_name, 'wb') as file:
            file.write(down_res.content)
        # 解压文件
        zip_file = zipfile.ZipFile(file_name)
        zip_file.extractall(save_file)
        print("extracting successfully")
        zip_file.close()
    except Exception as e:
        print(e)
    pass


def exe_open():
    try:
        pathDir = os.listdir(save_file)
        exe_name = ""
        exe_list = []
        for each in pathDir:
            if re.match(".*exe", each):
                exe_list.append(each)
        if len(exe_list) > 1:
            for each in exe_list:
                if re.match("LOL.*", each):
                    continue
                else:
                    exe_name = each
                    break
        else:
            exe_name = exe_list[0]
        exe_name = save_file + "/" + exe_name
        os.startfile(exe_name)
    except Exception as e:
        print(e)
    pass


if __name__ == "__main__":
    gethtml()
    geteditionNow()
    if url_edition > file_edition:
        print("prepare for downloading")
        exe_download()
    else:
        print("has been updated,waiting for launching")
    sys.stdout.flush()
    # sleep(2)
    exe_open()
    sleep(3)
