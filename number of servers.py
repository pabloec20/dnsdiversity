import csv
import time
from time import sleep
from publicsuffix import fetch
from publicsuffix import PublicSuffixList
from collections import Counter
from math import log, fsum
from decimal import *

servers=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
with open('myfile.csv', 'rb') as g:
	reader = csv.reader(g)
	for row in reader:
		print row[0]
		if "ERROR" not in row[1]:
			servers[len(row[1:])]=servers[len(row[1:])]+1
		print servers