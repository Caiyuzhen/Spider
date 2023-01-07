import requests
import bs4

"""UA 伪装"""
headers = {
	"user-agent": 
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.3"
}


"""请求网页"""
res = requests.get("https://www.douban.com/doulist/30299/", headers=headers)
# print(res)



"""解析网页中的内容（图片/文字）"""
soup = bs4.BeautifulSoup(res.text,"html.parser") #把 res 抓取的文本给到它, 并指定解析器
targets = soup.find_all("div", class_="title") #因为 class 是关键字，所以要加下划线来跟 class 关键字区分一下



"""打印数据"""
import time #导入时间库

def find_Movie():
	for each in targets:
		time.sleep(1) #加个延时，避免打崩网站
		print(each.a.text)

	print('Done!')
	

find_Movie()




