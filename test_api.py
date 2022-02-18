#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 #
# @Time    : 2022/1/6 23:28
# @Author  : sml2h3
# @Email   : sml2h3@gmail.com
# @File    : test_api.py
# @Software: PyCharm
import base64
import json
import requests

print(' ')
# ******************OCR识别部分开始******************
host = "http://127.0.0.1:9898"
# 目标检测就把ocr改成det,其他相同
# 方式一
file = open(r'test.jpg', 'rb').read()
# file = open(r'test_calc.png', 'rb').read()


api_url = f"{host}/ocr/file"
resp = requests.post(api_url, files={'image': file})
print(f"{api_url=}, {resp.text=}")

api_url = f"{host}/ocr/file/json"
resp = requests.post(api_url, files={'image': file})
print(f"{api_url=}, {resp.text=}")

api_url = f"{host}/ocr/b64"
resp = requests.post(api_url, data=base64.b64encode(file).decode())
print(f"{api_url=}, {resp.text=}")

api_url = f"{host}/ocr/b64/json"
resp = requests.post(api_url, data=base64.b64encode(file).decode())
print(f"{api_url=}, {resp.text=}")

api_url = f"{host}/det/file"
resp = requests.post(api_url, files={'image': file})
print(f"{api_url=}, {resp.text=}")

api_url = f"{host}/det/file/json"
resp = requests.post(api_url, files={'image': file})
print(f"{api_url=}, {resp.text=}")

# 滑块识别

target_file = open(r'match_target.png', 'rb').read()
bg_file = open(r'match_bg.png', 'rb').read()

api_url = f"{host}/slide/match/file"
resp = requests.post(api_url, files={'target_img': target_file, 'bg_img': bg_file})
print(f"{api_url=}, {resp.text=}")

api_url = f"{host}/slide/match/file/json"
resp = requests.post(api_url, files={'target_img': target_file, 'bg_img': bg_file})
print(f"{api_url=}, {resp.text=}")

api_url = f"{host}/slide/match/b64"
target_b64str = base64.b64encode(target_file).decode()
bg_b64str = base64.b64encode(bg_file).decode()
jsonstr = json.dumps({'target_img': target_b64str, 'bg_img': bg_b64str})
resp = requests.post(api_url, data=base64.b64encode(jsonstr.encode()).decode())
print(f"{api_url=}, {resp.text=}")

api_url = f"{host}/slide/match/b64/json"
resp = requests.post(api_url, data=base64.b64encode(jsonstr.encode()).decode())
print(f"{api_url=}, {resp.text=}")

target_file = open(r'compare_target.jpg', 'rb').read()
bg_file = open(r'compare_bg.jpg', 'rb').read()

api_url = f"{host}/slide/compare/file"
resp = requests.post(api_url, files={'target_img': target_file, 'bg_img': bg_file})
print(f"{api_url=}, {resp.text=}")

api_url = f"{host}/slide/compare/file/json"
resp = requests.post(api_url, files={'target_img': target_file, 'bg_img': bg_file})
print(f"{api_url=}, {resp.text=}")

api_url = f"{host}/slide/compare/b64"
target_b64str = base64.b64encode(target_file).decode()
bg_b64str = base64.b64encode(bg_file).decode()
jsonstr = json.dumps({'target_img': target_b64str, 'bg_img': bg_b64str})
resp = requests.post(api_url, data=base64.b64encode(jsonstr.encode()).decode())
print(f"{api_url=}, {resp.text=}")

api_url = f"{host}/slide/compare/b64/json"
resp = requests.post(api_url, data=base64.b64encode(jsonstr.encode()).decode())
print(f"{api_url=}, {resp.text=}")

# 方式二

# 获取验证码图片
# headers = {
#     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4195.1 Safari/537.36"
# }
# resp = requests.get('https://data.gdcic.net/Dop/CheckCode.aspx?codemark=408.15173910730016', headers=headers, verify=False)
# captcha_img = resp.content
#
# 识别
# resp = requests.post(api_url, files={'image': captcha_img})
# print('验证码结果', resp.text)
#
# # 保存验证码图片以供验证
# with open('captcha.jpg', 'wb') as f:
#     f.write(captcha_img)

# ******************OCR识别部分开始******************
