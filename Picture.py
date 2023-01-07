"""UA 伪装"""
headers = {
	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}


"""请求网页"""
import requests #导入 api 请求库
response = requests.get('http://www.vmgirls.com/12985.html', headers=headers)
html = response.text
# print(response.request.headers)
# print(response.text)


"""解析网页中的内容（图片/文字）"""
import re #导入正则表达式库, #re 是正则表达式的缩写
urls = re.findall('<a href="(.*?)" alt=".*?" title=".*?">', html)  #得到所有图片的地址
print(urls) 


"""保存数据"""
import time #导入时间库
for url in urls:
	time.sleep(1) #加个延时，避免打崩网站
	#给图片命名
	img_name = url.split('/')[-1] #取 url 最后一段作为名字
	response = requests.get(url, headers=headers)
	with open(img_name, 'wb') as f: #保存到本地文件夹
		print("图片下载成功!")
		f.write(response.content)


