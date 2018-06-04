#coding:utf-8
import requests
import  json

header = {

}
payload = {"yoyo":"hello word",
           "balabala":"222"}
data_json = json.dumps(payload)
r = requests.post('http://lxt.wgp.test.4000669696.com/login',json=data_json)
