import urllib2
import csv
from bs4 import BeautifulSoup
import io
import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import math
wiki = "https://www.techcrunch.com"
page = urllib2.urlopen(wiki)
soup = BeautifulSoup(page,"lxml")
stop_words = set(stopwords.words('english'))
all_p=soup.find_all("p")
with open('index.csv', 'a') as csv_file:
	writer = csv.writer(csv_file)
	for para in all_p:
		words=para.getText().encode('UTF-8').split()
		for r in words:
			if not r in stop_words:
				appendFile = open('filteredtext.csv','a')
				appendFile.write(" "+r)
				text_string = para.getText().encode('UTF-8').lower()
		frequency = {}
		match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
		hashmap={}
		for word in match_pattern:
		    count = frequency.get(word,0)
		    frequency[word] = count + 1
		frequency_list = frequency.keys()
		for words in frequency_list:
		    hashmap[words]=frequency[words]
		for element in hashmap:
		    print element,hashmap[element]
		    appendFile = open('tf_hashmap.csv','a')
		    appendFile.write(" "+element+" ")
		    appendFile.write(str(hashmap[element]))
		entropy=0
                words=para.getText().encode('UTF-8').split()
                for ele in frequency_list:
                    #print ele
                    entropy=entropy-(hashmap[ele]*math.log(hashmap[ele]))
                    print entropy
                print "hi"
                print entropy  
