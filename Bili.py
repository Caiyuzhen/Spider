import requests
import bs4
import time #导入时间库



"""UA 伪装"""
def openURL(url): #https://search.bilibili.com/all?keyword=%E7%BC%96%E7%A8%8B&search_source=5&page=1
	#https://search.bilibili.com/all?keyword=%E7%BC%96%E7%A8%8B&search_source=5&page=2&o=36
	headers = {
		"user-agent": 
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
	}

	res = requests.get(url, headers=headers)
	# print(res.text)
	return res






"""最终收集数据"""
def getData(res):
	
	#解析网页中的内容（图片/文字）
	soup = bs4.BeautifulSoup(res.text, "html.parser") #把 res 抓取的文本给到它, 并指定解析器
	allTitles = []
	titles = soup.find_all("h3", class_="bili-video-card__info--tit")

	print('😄开始获取数据...')

	for each in titles:
		time.sleep(1) #加个延时，避免打崩网站
		print(each.text)
		allTitles.append(each.text)
		
	return allTitles





"""返回页数"""
def getPageNum(res):
	soup = bs4.BeautifulSoup(res.text, "html.parser")
	pageNum = soup.find_all('button', class_='vui_button vui_button--no-transition vui_pagenation--btn vui_pagenation--btn-num')
	if pageNum:
		print(pageNum.text)
		return int(pageNum[-1].text) #返回最后一个页码
	else:
		return 28
	# return 28 #写死的方式





"""主运行函数"""
def mainFn():
	# host = "https://search.bilibili.com/all?keyword=%E7%BC%96%E7%A8%8B&search_source=5&page="
	# host = "https://search.bilibili.com/all?keyword=%E7%BC%96%E7%A8%8B&search_source=5&page={}&o={}"
	host = "https://search.bilibili.com/all"
	resAll = openURL(host) #发送请求, 返回一个初始地址（all 全集，然后去算出页数）
	pages = getPageNum(resAll)
	data = [] #⚡️⚡️最终搜集出来的数据

	for i in range(pages):
		# url = host + "&page=" + str(i+1) #拼接出每一页的 url
		url = host + '?keyword=%E7%BC%96%E7%A8%8B&search_source=5&page={}&o={}'.format(i+1, 36*i) #拼接出每一页的 url
		print(url)	
		res = openURL(url) #发送请求
		data.extend(getData(res)) #⚡️⚡️把每一页的数据都添加到 data 中
		

	with open('B站编程视频.txt', 'w', encoding='utf-8') as f: #🔥🔥把爬取的数据写入到文件中
		for each in data:
			f.write(each + '\n')



mainFn()

