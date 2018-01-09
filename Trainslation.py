# -*- coding: utf-8 -*-
import requests, json
from urllib.request import quote

# Geogle翻译API地址
# https://translate.google.cn/translate_a/single?
# client=t&sl=zh-CN&tl=en&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&ssel=3&tsel=3&kc=0&tk=607173.995236&
# q=%E4%BD%A0%E4%BB%AC%E5%A5%BD   PS：经过url编码转换的“你们好”

# 基准网址：https://translate.google.cn/translate_a/single?
url_pre = "https://translate.google.cn/translate_a/single?"

''' 中文转换成英文'''
query_param = "client=t&sl=zh-CN&tl=en&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&ssel=3&tsel=3&kc=0&tk=607173.995236&"
text = "你们好"  # 需要翻译的文本
text = "q=" + quote(text)  # 进行url编码然后加入到参数中

url = url_pre + query_param + text  # 将参数放置到url请求当中

r = requests.post(url)
translate_object = json.loads(r.text)
print("完整返回json字符串:" + r.text)
translate_transform = translate_object[0][0][0]  # 翻译的译文
translate_original = translate_object[0][0][1]  # 翻译的原文

'''英文转换成中文'''
query_param2 = "https://translate.google.cn/translate_a/single?client=t&sl=zh-CN&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&ssel=6&tsel=3&kc=0&tk=926763.542794&"
text2 = "How are you"
text2 = "q=" + quote(text)  # 进行url编码然后加入到参数中
url2 = url_pre + query_param + text2  # 将参数放置到url请求当中
r2 = requests.post(url2)
translate_object2 = json.loads(r2.text)
print("完整返回json字符串:" + r2.text)
translate_transform2 = translate_object2[0][0][0]  # 翻译的译文
translate_original2 = translate_object2[0][0][1]  # 翻译的原文