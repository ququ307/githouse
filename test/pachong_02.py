# -*— coding = utf-9 -*-
# 
# Author:Eric
# @softwarm:
import random
import urllib.request
import urllib.parse
import string


#
# def get_params():
#     url = "http://www.baidu.com/s?"
#     params = {
#         "wd":"中文",
#         "key":"zhang",
#         "value":"San"
#     }
#     #字典传参的中文解释
#     str_params = urllib.parse.urlencode(params)
#     print(str_params)
#     final_url = url + str_params
#     print(final_url)
#
#     #将带有中文的url转换为计算机可以识别的url
#     end_url = urllib.parse.quote(final_url,safe=string.printable)
#     print(end_url)
#     response = urllib.request.urlopen(end_url)
#
#     data = response.read().decode()
#     print(data)
#     with open("02_json_params_geturl.html","w",encoding='utf-8') as f:
#         f.write(data)
#



#get_params()


#handler处理器的定义
#

#请求头的设置


# def load_baidu():
#     url = "http://www.baidu.com"
#     #添加请求头
#     header = {
#         "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
#     }
#
#     #User-Agent列表
#     list_User_Agent = [
#         "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
#         "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.2.28) Gecko/20120306 Firefox/3.6.28",
#         "Mozilla/5.0 (Windows NT 5.1; rv:2.0) Gecko/20100101 Firefox/4.0",
#         "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.33 Safari/535.11",
#         "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)"
#
#     ]
#     #每次请求的浏览器都是不一样的
#     randon_user_agent = random.choice(list_User_Agent)
#
#
#
#
#     #创建请求头
#     request = urllib.request.Request(url)
#     print(request)
#     # request = urllib.request.Request(url,headers=header)
#     #动态的添加请求头信息
#     request.add_header("User-Agent",randon_user_agent)
#
#
#     #请求网络数据
#     response = urllib.request.urlopen(request)
#     print(response)
#     data = response.read().decode()
#
#     #响应头
#     #print(response.headers)
#     #获取请求头的信息
#     request_headers = request.headers
#     # request_headers = request.get_header('User-Agent')
#     print(request_headers)
#     with open("02header.html",'w',encoding='utf-8') as f:
#         f.write(data)

#       IP代理
#免费的IP(时效性差，错误率高)
#付费的IP()
#IP分类：透明(对方知道我们真是的IP)，匿名（对方不知道我们真实的IP，知道使用了代理），高密（不知真实的IP，不知使用了代理）
#
#




# def handler_openner():
#
#
#     #系统的urlopen并没有添加代理的功能所以需要我们之定义这个功能
#     #http：80
#     #https:443
#     #urlopen为什么可以请求数据，handler处理器
#     #自己的openner请求数据
#
#
#     url = "https://csdnnews.blog.csdn.net/article/details/109504424"
#
#     #创建自己的处理器
#     handler = urllib.request.HTTPHandler()
#     #创建自己的openner
#     openner = urllib.request.build_opener(handler)
#     #用自己的openner去请求数据
#     response = openner.open(url)
#     data = response.read()
#     print(data)
#
# handler_openner()





# def create_proxy_handler():
# #     url = "https://csdnnews.blog.csdn.net/article/details/109504424"
# #
# #     #添加代理
# #     proxy = {
# #         #免费的写法
# #         # "http":"171.12.115.186:9999"
# #         #付费的写法
# #         #
# #     }
# #
# #     #代理处理器
# #     proxy_handlder = urllib.request.ProxyHandler(proxy)
# #     #创建自己的openner
# #     openner = urllib.request.build_opener(proxy_handlder)
# #     #用代理IP去发送请求
# #     data = openner.open(url).read()
# #     print(data)
# #
# # create_proxy_handler()



#系统的urlopen()不支持代理的添加
#创建对应的处理器
#代理处理器proxyHandler
#拿着ProxyHandler创建openner  bulid_openner






def proxy_user():
    proxy_list = [
        {
            "http":"36.248.129.221:9999"
        },
        {
            "http":"175.42.122.245:9999"
        },
        {
            "http":"124.117.100.17:8118"
        },
        {
            "http":"123.56.118.36:8080"
        },
        {
            "http":"113.204.164.194:8080"
        }

    ]

    for proxy in proxy_list:
        print(proxy)
        #利用遍历出来的ip创建处理器
        proxy_handler = urllib.request.ProxyHandler(proxy)
        #创建openner
        openner = urllib.request.build_opener(proxy_handler)
        try:
            openner.open("https://www.baidu.com",timeout=1)
            print("haha")

        except Exception as e:
            print(e)

proxy_user()











