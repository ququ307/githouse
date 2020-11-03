# -*— coding = utf-9 -*-
# 
# Author:Eric
# @softwarm:

import urllib.request
import urllib.parse
import string
# def load_data():
#     url = "http://www.baidu.com/"
#     response = urllib.request.urlopen(url)
#     print(response)
#     #读取内容 bytes类型
#     data = response.read()
#     print(data)
#     #将文件获取的内容转换为字符串
#     str_data = data.decode("utf-8")
#     print(str_data)
#     with open("baidu.html","w",encoding="utf-8") as f:
#         f.write(str_data)
#     #将字符串类型转换为bytes
#     str = "baidu.com"
#     bytes_anme = str.encode("utf-8")
#     print(bytes_anme)

    #python爬取的类型：str bytes
    #如果爬取的类型是bytes类型，但是写入的时候需要字符串 decode("utd-8")
    #如果爬取的类型是str类型，但写入的是bytes类型  encode("utf-8")



# load_data()

def get_method_params():
    url = "http://www.baidu.com/s?wd="
    #拼接字符串(汉字)
    name = "美女"
    final_url = url+name
    print(final_url)
    #代码发送了请求
    #但请求里面包含了汉字；ascii是没有汉字的；url转译

    #发送网络请求
    #将包含汉字的url进行转译
    encode_new_url = urllib.parse.quote(final_url,safe=string.printable)
    print(encode_new_url)
    response = urllib.request.urlopen(encode_new_url)
    print(response)
    #python是解释性语言；解释器只支持ascii 0-127

    #读取内容
    data = response.read().decode()
    print(data)
    #保存到本地
    with open("02-encode.html",'w',encoding='utf-8') as f:
        f.write(data)

get_method_params()



