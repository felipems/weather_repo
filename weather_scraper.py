#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""
DESCRIPTION GOES HERE
"""

import sys
import os
import csv
import random
from lxml import html
from bs4 import BeautifulSoup
import requests
import urllib
import re
def main():

	r = urllib.urlopen('http://10.0.0.55/livedata.htm').read()
	soup = BeautifulSoup(r, 'lxml')
	print "done"
	
	data_points = soup.find_all("input", class_="item_2")

	for elem in data_points:
		# print elem
		e_list =  str(elem).split("=")
		print re.search('.*"' ,e_list[4]).group(0).replace('"', "")
		print re.search('.*"', e_list[-1]).group(0).replace('"', "")
		print ""



if __name__ == "__main__":
	sys.exit(main()) 






# from bs4 import BeautifulSoup
# import urllib
# r = urllib.urlopen('http://www.aflcio.org/Legislation-and-Politics/Legislative-Alerts').read()
# soup = BeautifulSoup(r)
# print type(soup)
