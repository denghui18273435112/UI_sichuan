import requests

from config import ConfigYaml
from tools import my_log


#重构requests库中的post方法、get方法  使用中
class Request:

	def __init__(self):
		self.log = my_log("自定义封装")

	def request_api(self,url,headers=None,data=None,json=None,cookies=None,method="get"):
		"""
		:param url: 必传
		:param headers: 默认不传
		:param data: 默认不传
		:param json: 默认不传
		:param cookies: 默认不传
		:param method: 默认为get
		:return:  res字典由code和body组成
		#status_code获取状态码
		"""
		if method=="get":
			self.log.debug("发送get请求")
			r = requests.get(url=url,headers=headers,data=data,cookies=cookies)
		elif method=="post":
			self.log.debug("发送post请求")
			r = requests.post(url=url,headers=headers,data=data,json=json,cookies=cookies)
		try:
			body = r.json()
		except Exception as e:
			body = r.text
		res =dict()
		res["code"] = r.status_code
		res["body"] = body
		return res

	def new_get(self,url,**kwargs):
		"""
		:param url:  接口地址
		:param kwargs: 不定参数: *args和**kwargs 可以接受任意长度和格式的参数；两个参数不能同时传，一次只能传一个
		:return: 调用request_api方法,method默认为get,并且传入随意参数;request_api方法支持headers,docs,json,cookies
		"""
		return self.request_api(url,method="get",**kwargs)

	def post(self,url,**kwargs):
		"""
		:param url:  接口地址
		:param kwargs: 不定参数: *args和**kwargs 可以接受任意长度和格式的参数；两个参数不能同时传，一次只能传一个
		:return: 调用request_api方法,method默认为post,并且传入随意参数;request_api方法支持headers,docs,json,cookies
		"""
		return self.request_api(url,method="post",**kwargs)

if __name__ == '__main__':
	url = ConfigYaml().get_conf_url()+"/authorizations/"
	data = {"username":"python","password":"12345678"}
	print(Request().post(url=url,data=data))