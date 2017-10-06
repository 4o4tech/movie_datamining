#/usr/bin/python
# -*- coding:utf-8 -*-
import re
import requests
import urllib
import os
from bs4 import BeautifulSoup
from urllib2 import HTTPError



def getHtml(url):
    head = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'#,
        #'Cookie:'
    }
    try:
        req = requests.get(url, headers=head)
        return req.text
    except requests.ConnectionError as e:
        return None

#get name and
def getData(htmltext):
	# s = re.sub('<br\s*?>', '', htmltext)
    soup = BeautifulSoup(htmltext, 'html.parser')

    # f*ck br tag make me suck
    for tag in soup.find_all(re.compile("br")):
    	tag.unwrap()
    	
    # print soup
    pTag = soup.find_all('div',{'class':'yn'})

    #find <b>Author:</b>
    author_string = soup.find_all(string=re.compile("Author:"))

    author_name = []
    comments = []

    finalData ={}

    count = 0 
    for x in author_string:
    	#author information div
    	author_infor = x.find_parent("div")
    	
    	# tag p is comment
    	comment = author_infor.find_next("p")

    	#merge split comment together
    	strComment = ''
    	for i in comment:
    		strComment += i

    	# add to comments list
    	comments += strComment
 
    	# author name, a tag content in the div
    	aList = author_infor.find_all('a')

    	author_name += aList[1].contents


    # for comment in comments:


    # for k  in author_name:
    # 	for v in comment:

    # 		finalData[k] = v
    # return finalData


    	# author_comment[author_name] = comment

    # return finalData

    # for i in pTag:
    #    commet = i.previous_sibling
    #    commet.previous_sibling
    #    print i



def main():

	#调试 ……  10/6 8:58
	#  imdb url  http://www.imdb.com/title/tt0137523/reviews?count=10&start=0
	#  movie id: tt0137523  
	#  comment number: count 
    url = 'http://www.imdb.com/title/tt0137523/reviews?count=10&start=0'
    htmltext = getHtml(url)

    # read local file html file
    '''
    module_path = os.path.dirname(__file__)    
    filename = module_path + '/test.html'
    read = open(filename,'r')
    htmltext = read.read()
    read.close()
    '''

    getData(htmltext)
    # infor = getHref(htmltext)

    # for k, v in infor.iteritems():
    # 	print k + "\n" +v


if __name__ =='__main__':
	main()


