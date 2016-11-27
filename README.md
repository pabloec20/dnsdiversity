# dnsdiversity

DNS Diversity Cathastrophy Part 1.
Why was it so easy for the Mirai botnet to make so much damage? Is the internet that weak? What if it happens again? what can we do about it?


A month ago, I was asking myself those questions as an unprecedented attack against the internet infrastructure was disrupting service to some of the very big names of the internet. Now we know that the attackers directed their efforts against just one DNS provider. The lesson learned was obvious, the standard two DNS servers approach was insufficient if the two servers were from the same company, if your DNS company went down you went with them.


The problem was widespread, but how much? I decided to find out, following that path I just discovered how weak the internet really is and how can botnets maximize their impact if they play their numbers well.
The problem and how to measure it.
I needed a metric that would not only take into account how many DNS servers the domain was using but also would take into account how many different DNS providers it was using. There is a similar problem in biology when measuring the diversity of species in a plot of land, the solution is the Shannon Diversity Index, which not only takes into account the number of individuals, but also the distribution of those individuals among different species.
I queried the NS records of the Alexa's Top 1Million Websites List, 62% of the sites have only two name servers, but also more than 33% has more than 3 name servers on their ns record (in about 4% of domains the query resulted in error), and about one percent of domains have a single hostname on their NS record

Looks good, until we see the actual diversity numbers as the Shannon index takes into account both the sheer number of servers(individuals) and whether they are of the same provider or not(species), we see a completely bleak ecosystem, if each domain is a plot of land, 82 percent of those plots have only one species inhabiting it, it means that in the new panorama where a single DNS provider means a single point of failure 82% of the internet top websites is susceptible to a DDOS attack.

Yes, the internet is weak, but how much weak is it? how do we calculate it? In part two I'm going to explain how to find it out.


All the code will be uploaded in my GitHub repository, please feel free to redo my calculations and double-check it. Also, no ns server was damaged while this data was gathered, it was harvested over 5 days at a rate of 2 queries per second so not to be a load to the DN system.
