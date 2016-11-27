import csv
import time
from time import sleep
from publicsuffix import fetch
from publicsuffix import PublicSuffixList
from collections import Counter
from math import log, fsum
from decimal import *

errors = 0
total = 0
with open('myfile.csv', 'rb') as g:
	reader = csv.reader(g)
	for row in reader:
		print row[0]
		if "ERROR" in row[1]:
			errors=errors+1
		total= total+1
		print errors
		print total