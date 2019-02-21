#! /usr/bin/env python

import urllib.request as urllib2
from bs4 import BeautifulSoup

#____________________________________________________________________________||

topNewsDict = {'id':'top-news','class':'top-news'}
firstColDict = {'class': 'first-column-region region'}
headDict = {'class': 'story-heading'}
summaryDict = {'class': 'summary'}

#____________________________________________________________________________||

url = "http://www.nytimes.com/"

page = urllib2.urlopen( url )
data = BeautifulSoup( page , "html.parser" )

#____________________________________________________________________________||

topNews = data.body.find( 'section', attrs = topNewsDict ).find('article')

#____________________________________________________________________________||

print

heading = topNews.find('h2', attrs = headDict )
print ("-"*len(heading.text))
print (heading.text)
print ("-"*len(heading.text))

#____________________________________________________________________________||

summary = topNews.find('p', summaryDict )
print (summary.text)

print 
#____________________________________________________________________________||

#____________________________________________________________________________||
