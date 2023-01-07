import csv
from selenium import webdriver #导入驱动模块（能够操作谷歌浏览器）,模拟用户点击行为, pip install selenium
driver = webdriver.Chrome() #建立驱动, 打开谷歌浏览器
driver.get('https://www.zhipin.com/web/geek/job?query=python&city=101280600')#打开网站

divs = driver.find_elements_by_css_selector('job-title')
for div in divs:
    job_name = div.find_element_by_css_selector('job-name').text
    print(job_name)
    
    with open('boss.csv', encoding='utf-8', mode='a') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([job_name])