# -*— coding = utf-9 -*-
# 
# Author:Eric
# @softwarm:
import requests
url = 'http://www.baidu.com'
response = requests.get(url)
#response返回的是bytes类型
data = response.content.decode()
print(data)