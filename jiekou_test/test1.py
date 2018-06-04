#coding:utf-8
import  requests

import  json



r = requests.get("http://www.baidu.com")
req = r.status_code
print req