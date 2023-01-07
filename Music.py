import requests
import bs4
import re #正则表达式内置模块
import time #导入时间库

def get_List(tragetUrl):
	# UA 伪装
	headers = {
		"user-agent": 
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
			# "refer": "https://music.163.com/" #指定请求来源， 可以在 request header 中找到
	}


	# 发起请求
	res = requests.get(tragetUrl, headers=headers)
	html_data = re.findall('<a href="/song\?id=(\d+)">(.*?)</a>', res.text) #用正则表达式匹配标签, 返回的是一个元组对象
	# print(html_data)


	#定义一个存放 id、title、二进制音乐文件 的列表
	music_list = []

 
 	# 遍历音乐数据
	for num_id, title in html_data:
		# print(num_id, title)
		time.sleep(0.5) #加个延时，避免打崩网站
		music_url = f'https://music.163.com/song/media/outer/url?id={num_id}.mp3'
		music_content = requests.get(url=music_url, headers=headers).content #对音乐地址发送数据, 接收二进制的音乐文件
		music_list.append([num_id, title, music_content]) #将 id、title、二进制音乐文件 添加到列表中
		# music_list.append([num_id, title])
  
	#返回数据
	return music_list



    

# 核心调用函数
def main():
	# url = input("请输入歌单连接地址") #拿到 url
	url = 'https://music.163.com/discover/toplist?id=3778678' #记得是 request header 中的地址！二级路由！!

	resMusicData = get_List(url) #传递给函数(返回的是音乐的  id、title、二进制音乐文件 三种数据！)
	print(resMusicData)

	with open("music.txt", "w", encoding="utf-8") as file:
		file.write(resMusicData)
  
	with open('music\\' + resMusicData.title + '.mp3', mode='wb') as file:
		file.write(resMusicData.music_content)


if __name__ == "__main__":
	main()