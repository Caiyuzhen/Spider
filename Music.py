import requests
import bs4
import re #正则表达式内置模块
import time #导入时间库
import json #把列表转为 json 格式
import os #导入 os 模块(文件操作模块)


def get_List(tragetUrl):
	# UA 伪装
	headers = {
		"user-agent": 
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
			# "refer": "https://music.163.com/" #指定请求来源， 可以在 request header 中找到
	}


	# 发起请求
	res = requests.get(tragetUrl, headers=headers)
	html_data = re.findall('<a href="/song\?id=(\d+)">(.*?)</a>', res.text) #用正则表达式匹配标签, 返回的是一个个元组对象
	# print(html_data)


	#定义一个存放 id、title、二进制音乐文件 的列表
	music_list = []


	print('获取数据...')
 	# 遍历音乐数据
	for num_id, title in html_data:
		# print(num_id, title)
		time.sleep(0.5) 
		music_url = f'https://music.163.com/song/media/outer/url?id={num_id}.mp3' #单独解析出音乐地址
		music_content = requests.get(url=music_url, headers=headers).content #对音乐地址发送数据, 接收二进制的音乐文件
  
		music_list.append({'num_id': num_id, 'title': title, 'music': music_content}) #以字典的形式存入数据
  
	#返回数据
	return music_list



    

# 核心调用函数
def main():
	url = 'https://music.163.com/discover/toplist?id=3778678' #👈如果要修改爬取地址, 那么只要改这个榜单 id 就可以了, 记得是 request header 中的地址！二级路由！!
	# url = input("请输入歌单连接地址") #拿到 url

	resMusicData = get_List(url) #传递给函数(返回的是音乐的  id、title、二进制音乐文件 三种数据！) 此时还是字典格式的数据！
 
 
	#🔥保存 id 跟标题
	with open("music.txt", "w", encoding="utf-8") as file:
		#判断如果是标题数据才保存
		for musicData in resMusicData:
			num_id = musicData['num_id'] #遍历出音乐 id
			title = musicData['title'] #遍历出音乐标题
			file.write(num_id + ' ' + title + '	' + '\n') #写入文件
			print(num_id, title)


 	#🔥创建文件夹, 保存音乐文件
	fileName = 'musicDownload\\'
	if not os.path.exists(fileName):#如果没有这个文件夹那么久创建一个文件夹
		os.makedirs(fileName)

	for musicData in resMusicData:
		print('🎵音乐下载中...')
		title = musicData['title'] #遍历出音乐标题
		musicFile = musicData['music'] #遍历出音乐下载地址
		with open(fileName + title + '.mp3', mode='wb') as file:
			file.write(musicFile)


if __name__ == "__main__":
	main()
 
#reference: https://www.bilibili.com/video/BV1b8411K7n5/?p=2&spm_id_from=333.880.my_history.page.click&vd_source=b67f9398d85e7e297041f47a430b16cb