# -*- coding: utf-8 -*- 
#from urllib import request
import requests

if __name__ == "__main__":
	print("Start")
	response = requests.get("http://www.sse.com.cn/js/common/detachableConvertibleBulletin/convertiblebulletin_new.js?_=1578930584168")
	response.encoding = 'utf-8'
	print(response.text)
	