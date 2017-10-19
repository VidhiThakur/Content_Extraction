import urllib2
import csv
from bs4 import BeautifulSoup

wiki = "https://en.wikipedia.org/wiki/Facebook"
#"https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
page = urllib2.urlopen(wiki)
soup = BeautifulSoup(page,"lxml")
#print soup.prettify().encode('UTF-8')
all_p=soup.find_all("p")
with open('index.csv', 'a') as csv_file:
	writer = csv.writer(csv_file)
        for para in all_p:
	    #this is to be stored in csv 
	    #print para.getText().encode('UTF-8')
	    writer.writerow([para.getText().encode('UTF-8')])
	    #writer.writerow("\n")

