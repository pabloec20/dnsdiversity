import csv
import time
from time import sleep
from publicsuffix import fetch
from publicsuffix import PublicSuffixList
from collections import Counter
from math import log, fsum

#fetch the dns public suffix list from https://publicsuffix.org/list/public_suffix_list.dat
psl_file = fetch()

psl = PublicSuffixList(psl_file)
start_time = time.time()

with open('myfile.csv', 'rb') as g:
	reader = csv.reader(g)
	out = csv.writer(open("shannon.csv","ab"), delimiter=',')
	for row in reader:
		tldlist = []
		nslist = []
		frequencies = []
		nslist.append(row[0])
		if "ERROR" not in row[1]:
			summa=len(row[1:])
			for ns in row[1:]:
				tld=psl.get_public_suffix(ns)
				tldlist.append(tld)
			newlist = Counter(tldlist).values()
			floatlist = [float(i) for i in newlist]
			for count in floatlist:
				(frequencies.append(-1*(count/summa)*log(count/summa)))
			shannon=fsum(frequencies)
			nslist.append(shannon)	
		print nslist
		out.writerow(nslist)
	out.writerow(time.time()-start_time)