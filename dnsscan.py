import dns.resolver
import csv
import time
from time import sleep
start_time = time.time()

with open('1m.csv', 'rb') as g:
    reader = csv.reader(g)
    for row in reader:
	sleep(2)
	host = row[1]
	try:
		answers = dns.resolver.query(host, 'NS')
	except (KeyboardInterrupt, SystemExit):
        	raise
	except:
		answers = "ERROR "
	out = csv.writer(open("myfile.csv","a"), delimiter=',')
	hosto=host+" "
	newhost=hosto+' '.join(str(f) for f in answers)
	newhost=newhost.split( )
	print host 
	out.writerow(newhost)
print("--- %s seconds ---" % (time.time() - start_time))
