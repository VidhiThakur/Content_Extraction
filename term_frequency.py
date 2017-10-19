import re
import string
frequency = {}
document_text = open('filteredtext.csv', 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
hashmap={}
for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1
     
frequency_list = frequency.keys()
 
for words in frequency_list:
    hashmap[words]=frequency[words]
    #print words, frequency[words]
for element in hashmap:
    print element,hashmap[element]
    appendFile = open('tf_hashmap.csv','a')
    appendFile.write(" "+element+" ")
    appendFile.write(str(hashmap[element]))
    appendFile.close()


