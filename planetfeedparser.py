#!/usr/bin/env python
import feedparser
import sys

def printer(data):
    pass


def process_feed(link):
    """
    Function to process feeds and prints post titles and author.
    """
    #Parsing the document
    feed = feedparser.parse(link)

    #Counting total posts
    total_posts = len(feed.entries)


    #Fectching author & post titles from 'feed' object
    author_title = feed.entries[0].title.split(": ")
    author = author_title[0]
    post_title = author_title[1]
    print author + '\n' + post_title



















#List index
        #i=0
        #length= len(author_title)
        #author=''
        #post_title=''
        
        #Fetching author
       # while author_title[i] != ':':
         #   author = author + author_title[i]
        #    i +=1
        #Fetching title
       # while i < length:
       #     post_title = post_title + author_title[i]
       #     i +=1
      #  count += 1
       # 
        #Printing
    #    print str(count) + ': Post Title' + post_title
    #    print '        Author: ' + author
        
        #It is optional part when argument -l or --link given then only it will be execute and show all the link to the respective posts
      #  if flag == 1:
        #    post_link=feed.entries[count-1].link
         #   print '         Link: ' + post_link + '\n'
