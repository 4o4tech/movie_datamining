# /usr/bin/python
# -*- coding:utf-8 -*-
import re
import requests
import urllib
import os
import time
import csv

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

    author_name_list = []
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



        # for i in comment:
        # 	strComment += i  

        # add to comments list
        comments.append(comment)

        # author name, a tag content in the div
        aList = author_infor.find_all('a')

        name = aList[1].contents

        author_name_list.append(name)

    


    


    with open('data.txt','a') as myfile:
        for i in range(0,len(comments)):

            myfile.write(''.join(author_name_list[i]))

            myfile.write(''.join(comments[i]))
        
        # print author_name_list[i]

        # print  comments[i]


    # for i in pTag:
    #    commet = i.previous_sibling
    #    commet.previous_sibling
    #    print i


def getUrl():
    pass


def main():

	#调试 ……  10/6 8:58
	#  imdb url  http://www.imdb.com/title/tt0137523/reviews?count=10&start=0
	#  movie id: tt0137523  
	#  comment number: count

    urlList={'tt0071562':'50'}

    # urlList={'tt0111161':'4796','tt0068646':'2475','tt0071562':'699'}

    for x in urlList:
        
        url = 'http://www.imdb.com/title/'+ x +'/reviews?count='+urlList[x] +'&start=0'

        print url
        print " <-_-> "*20

        htmltext = getHtml(url)

        infor = getData(htmltext)



    # url = 'http://www.imdb.com/title/tt0137523/reviews?count=10&start=0'
    # htmltext = getHtml(url)

    # read local file html file
    
    # # module_path    
    # filename = os.path.dirname(os.path.abspath(__file__)) + '/test.html'
    # read = open(filename,'r')
    # htmltext = read.read()
    # read.close()
    

    # getData(htmltext)
    
    #infor = getData(htmltext)


if __name__ =='__main__':

	main()


