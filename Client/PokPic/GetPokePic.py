#coding=utf-8
import urllib
import sys
import re
import os
import socket

# print re.findall(r'\d+','one1two2three3four4')
if not os.path.exists("url_html.txt"):
	print "does't find url_html.txt ..."
	print "start get url_html from website http://wiki.52poke.com ..."
	url = "http://wiki.52poke.com/zh/%E7%A5%9E%E5%A5%87%E5%AE%9D%E8%B4%9D%E5%88%97%E8%A1%A8%EF%BC%88%E6%8C%89%E5%85%A8%E5%9B%BD%E5%9B%BE%E9%89%B4%E7%BC%96%E5%8F%B7%EF%BC%89#.23001_-_.23151_.E5.A6.99.E8.9B.99.E7.A7.8D.E5.AD.90_-_.E5.A4.A2.E5.B9.BB"
	text = urllib.urlopen(url).read()
	file1 = open("url_html.txt","w").write(text)
else:
	print "find url_html.txt ..."
	print "start get url_html from file url_html.txt ..."
	text = open("url_html.txt","r").read()

if not os.path.exists("urls.txt"):
	print "does't find urls.txt ..."
	print "start get urls from file url_html.txt ..."
	pattern = r'''<td>#(\w{3})\n</td>\n<td>#\w{3}\n</td>\n<td><span class="sprite-icon sprite-icon-\w{3}" title=""></span>\n</td>\n<td><a href="(/wiki/.{,36})" title'''
	urllist = re.findall(pattern, text)
	file1 = open("urls.txt","w")
	urls = []
	for x in urllist:
		file1.write("http://wiki.52poke.com"+x[1]+'\n')
		urls.append("http://wiki.52poke.com"+x[1]);
	file1.close()
else :
	print "find urls.txt ..."
	print "start get urls from file urls.txt ..."
	file1 = open("urls.txt","r")
	urls = []
	for x in file1.readlines():
		urls.append(x)

#print urls

picurls = []
if not os.path.exists("picurls.txt"):
	print "does't find picurls.txt ..."
	print "start get picurls from file urls.txt ..."
	file1 = open("picurls.txt","w")
	for url in urls:
		pichtml = urllib.urlopen(url).read()
		pattern =r'''width="\d+" height="\d+" data-url="(//media.52poke.com/wiki/thumb/\w*/\w*/\d{3}[\w|%|\.|-]+.png/)\d+(px-\d{3}[\w|%|\.|-]+.png)" data-srcset="'''
		picurl = re.findall(pattern, pichtml)
		print picurl
		picurl = "http:"+picurl[0][0]+"120"+picurl[0][1]
		file1.write(picurl+'\n')
		picurls.append(picurl)
else :
	print "find picurls.txt ..."
	print "start get urls from file picurls.txt ..."
	file1 = open("picurls.txt","r")
	for x in file1.readlines():
		picurls.append(x)

socket.setdefaulttimeout(5)
print "start download files ..."
flag = True
while flag:
	flag = False
	for picurl in picurls:
		pattern =r'''120px-(\d{3})[\w|%|\.|-]+(.png)'''
		filenames = re.findall(pattern, picurl)
		filename = "Pics/"+filenames[0][0]+filenames[0][1]
		if not os.path.exists(filename):
			flag = True;
			try:
				urllib.urlretrieve(picurl, filename)
			except Exception, e:
				raise e
print "success ..."