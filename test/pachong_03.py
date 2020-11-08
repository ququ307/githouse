# -*— coding = utf-9 -*-
# 
# Author:Eric
# @softwarm:
import urllib.request

# def money_proxy_use():
#     #代理IP
#     money_proxy_use = {
#         "http":"username:pwd@IP地址:端口"
#     }
#     proxy_handler = urllib.request.ProxyHandler(money_proxy_use)
#     openner = urllib.request.build_opener(proxy_handler)
#     openner.open("http:www.baidu.com")
#     #第二种付费代理的IP地址
#     username = "name"
#     pwd = "passwd"
#     proxy_addr ="IP地址:端口"
#     #创建密码管理器,添加用户名和密码
#     password_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
#     password_manager.add_password(None,proxy_addr,username,pwd)
#     #创建Proxy代理
#     handler_auth_proxy = urllib.request.ProxyBasicAuthHandler(password_manager)
#     #创建openner
#     open_auth = urllib.request.build_opener(handler_auth_proxy)
#     #发送请求
#     open_auth.open("http:www.baidui.com")



def auth_nei_wang():
    user = "admin"
    pwd = "admin123"
    nei_url = "http://192.168.179.66"

    #创建密码管理器
    pwd_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    pwd_manager.add_password(None,nei_url,user,pwd)
    #创建认证处理器
    auth_handler = urllib.request.HTTPBasicAuthHandler(pwd_manager)

    openner =urllib.request.build_opener(auth_handler)
    response = openner.open(nei_url)
    print(response)
