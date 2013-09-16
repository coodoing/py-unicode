#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import concurrent.futures
import urllib.request

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/']

# Retrieve a single page and report the url and contents
def load_url(url, timeout):
    conn = urllib.request.urlopen(url, timeout=timeout)
    return conn.readall()

'''
	scrapy每次运行的结果不一致
'''
def scrapy():
	# We can use a with statement to ensure threads are cleaned up promptly
	with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
	    # Start the load operations and mark each future with its URL
	    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
	    for future in concurrent.futures.as_completed(future_to_url):
	        url = future_to_url[future]
	        try:
	            data = future.result()
	        except Exception as exc:
	            print('%r generated an exception: %s' % (url, exc))
	        else:
	            print('%r page is %d bytes' % (url, len(data)))



def excutor_callback():
	from concurrent.futures import ThreadPoolExecutor
	with ThreadPoolExecutor(max_workers=1) as executor:
		future = executor.submit(pow, 5, 5)
		print(future.result())


def time_test():
	import time


def deadlock():
	pass



if __name__ == "__main__":
	
	print(sys.meta_path)
	print(type(sys))
	print(sys.path)
	#print(sys.modules)
	print("__main__" in sys.modules)
	print("exceptions" in sys.modules)
	print("sys" in sys.modules)
	print("__builtin__" in sys.modules)

	#excutor callable
	excutor_callback()

	#urllib.request
	scrapy()
	#print(pow(400,1235))	
	