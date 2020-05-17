import requests
from bs4 import BeautifulSoup

def geturl(url):
	#请求详细页面
	header = {
	'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
	}
	r = requests.get(url, headers=header)
	r.encoding = "utf-8"
	return r.text

def getcontent(url):
	html = geturl(url)
	soup=BeautifulSoup(html,'html.parser')
	content = soup.find_all(name='div',attrs={"class":"acontent"})

	content = soup.select('.acontent')

	# print(type(content))
	# print(type(content[0]))

	# return content[0]

	content = str(content)

	content = content.replace('/uploadfile','http://news.cqu.edu.cn/newsv2/uploadfile')
	content = content.replace('http://news.cqu.edu.cn/newsv2http://news.cqu.edu.cn/newsv2',
	                          'http://news.cqu.edu.cn/newsv2')
	content = content.replace('"acontent"','"acontent" style="font-size:20px;text-indent: 2em;line-height:40px;"')

	return (content[1:-1])

url = 'http://news.cqu.edu.cn/newsv2/show-14-21838-1.html'

html = geturl(url)

print(getcontent(url))