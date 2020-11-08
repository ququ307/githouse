# -*— coding = utf-9 -*-
# 
# Author:Eric
# @softwarm:

import urllib.request
from http import   cookiejar #自动保存cookie
import urllib.parse
import string


#
# url = "https://pan.baidu.com/disk/home#/all?path=%2F&vmode=list"
# headers = {
#
#     "User-Agent":"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)"
#     ,
#     'Cookie':'BIDUPSID=9D4BA49111CCC56903944DB097EE2742; PSTM=1600956896; BAIDUID=9D4BA49111CCC569D6B6F8225FCDD522:FG=1; PANWEB=1; BDUSS=FNV29DRmV2bDUwY2h3UkpybnZ5WGd4amdZaWthVW00cG1jTmx3flQ5bkoyN3RmRVFBQUFBJCQAAAAAAAAAAAEAAACgoQC1wLRqZXQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMlOlF~JTpRfZl; BDUSS_BFESS=FNV29DRmV2bDUwY2h3UkpybnZ5WGd4amdZaWthVW00cG1jTmx3flQ5bkoyN3RmRVFBQUFBJCQAAAAAAAAAAAEAAACgoQC1wLRqZXQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMlOlF~JTpRfZl; BAIDUID_BFESS=47A01D530D0C5B1E38226DEC1FBECCBD:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; PSINO=1; H_PS_PSSID=32809_1452_33041_32706_32961; BA_HECTOR=018k018k8g2g80a5l21fqejf90p; BCLID=6770253258229015813; BDSFRCVID=Tc0OJexroG3oCojr6PErhj1ivSNbUdrTDYLEmQHHJkBXE_kVJeC6EG0Pts1-dEu-EHtdogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tR3j3Ru8KJjEe-Kk-PnVep0SD-nZKRvHa2keWhOO2t_-Vh54M-CaMJK9Xx5PKnjn3N5rKR6lWpnkjpoyQqnO3xI8LNj405OTbTADsRbNb66pO-bghPJvyT8sXnO7tfnlXbrtXp7_2J0WStbKy4oTjxL1Db3JKjvMtgDtVJO-KKCKMKP6jf5; STOKEN=7106b0513fd03c5b22bcd8f010738295610bd013502150e9a638fa929c14f99f; SCRC=0e6395fb83fa33c4b63f2bb7462dc0e5; PANPSC=10339288721147348753%3ACU2JWesajwCwhhKGNoIw4xGy4OU887ORtAgaxVg2qFCIzVpKJVEAHhM4dDjxBdlpXbYM2RDWN74nGYtpHPcUTaF198qoEZE31cOxG%2BadPe49i3WzCs4DQjGuaZCjAuzWYqZdy9zZ13nFd%2BczPBNYtzaPJvsmh0iKjFY%2Fj%2FLBUWg%3D; Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0=1604799979,1604800584; Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0=1604800584'
# }
# request = urllib.request.Request(url,headers=headers)
# response = urllib.request.urlopen(request)
# data = response.read().decode()
# print(data)
# with open("04_cookies-ok.html",'w',encoding='utf-8') as f:
#     f.write(data)

#代码登录
# def code_login():
#     #登录网址
#     login_url = "https://www.yaozh.com/login"
#     #登录参数
#     login_form_data = {
#         "username":'17607103720',
#         "pwd":"qweasdzxc.123",
#         "formhash":"0CE0E474DA",
#         "backurl":"https%3A%2F%2Fwww.yaozh.com%2F"
#
#     }
#     #
#     #转码登录参数
#     #参数需转译为bytes对象
#     parse_data = urllib.parse.urlencode(login_form_data).encode()
#     print(parse_data)
#
#     #发送登录请求
#     #cookie的处理
#     cook_jar = cookiejar.CookieJar()
#     #定义有cookie功能的处理器
#     cook_handler = urllib.request.HTTPCookieProcessor(cook_jar)
#     openner = urllib.request.build_opener(cook_handler)
#     #带着参数发送post请求
#     #参加请求头
#     headers = {
#         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"
#
#     }
#     login_request = urllib.request.Request(login_url,data=parse_data,headers=headers)
#     #如果登录成功自动保存cookie
#     openner.open(login_request)
#
#     #带着cookie去访问个人中心
#     center_url = "https://www.yaozh.com/member"
#     center_requset = urllib.request.Request(center_url,headers=headers)
#     response = openner.open(center_requset)
#     data  =response.read().decode()
#     with open('yaozhi_cookies_login.html','w',encoding='utf-8') as f:
#         f.write(data)
#
# code_login()

#多用户,多账号不同地点登录

#判断异常
# urllib.request.HTTPErrorProce

