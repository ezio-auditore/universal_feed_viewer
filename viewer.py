#!/usr/bin/env python
import argparse
import planetfeedparser

flag_view_links=0
post_needed=10


parser = argparse.ArgumentParser(description='Process feeds for you and view them on terminal')
parser.add_argument("-l", "--link", action="store_true",
                    help="Show all the links to original posts")
parser.add_argument("url", type = str, help= "Give the url")
parser.add_argument("-p", "--post", type =int, help="Give the number how many post you want")

args = parser.parse_args()
if args.link:
    flag_view_links=1
if args.post:
    post_needed=args.post

if __name__ == '__main__':
    feed_data=planetfeedparser.process_feed(args.url)
