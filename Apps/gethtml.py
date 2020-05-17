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
	content = str(content)
	content = content.replace('/uploadfile','http://news.cqu.edu.cn/newsv2/uploadfile')
	content = content.replace('http://news.cqu.edu.cn/newsv2http://news.cqu.edu.cn/newsv2',
	                          'http://news.cqu.edu.cn/newsv2')
	content = content.replace('"acontent"','"acontent" style="font-size:20px;text-indent: 2em;line-height:40px;"')

	#标题
	title = soup.select('.dtitle')[0]
	title = title.string

	#日期
	date = soup.select('.dinfob')[0]
	date = date.get_text

	#摘要
	abstract = soup.select('.adetail')[0]
	abstract = abstract.string


	return ({'content':content[1:-1],'title':title,'date':date,'abstract':abstract})



url = 'http://news.cqu.edu.cn/newsv2/show-14-21838-1.html'

html = geturl(url)

# print(getcontent(url))
# gettitle(url)
