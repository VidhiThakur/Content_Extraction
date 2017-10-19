'''from nltk.corpus import stopwords

tokenized_docs_no_stopwords = []
tokenized_docs_no_punctuation=[['Here', 'simple', 'basic', 'sentences'], ['They', 'wo', u'nt', 'interesting', 'I', u'm', 'afraid'], ['The', 'point', 'examples', u'learn', 'basic', 'text', 'cleaning', u'works', u'simple', 'data']]
for doc in tokenized_docs_no_punctuation:
    new_term_vector = []
    for word in doc:
        if not word in stopwords.words('english'):
            new_term_vector.append(word)
    tokenized_docs_no_stopwords.append(new_term_vector)
            
print tokenized_docs_no_stopwords'''
'''from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
 
example_sent = "This is a sample sentence, showing off the stop words filtration."
 
stop_words = set(stopwords.words('english'))
 
word_tokens = word_tokenize(example_sent)
 
filtered_sentence = [w for w in word_tokens if not w in stop_words]
 
filtered_sentence = []
 
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
 
print(word_tokens)
print(filtered_sentence)'''
import io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
#word_tokenize accepts a string as an input, not a file.
stop_words = set(stopwords.words('english'))
file1 = open("index.csv")
line = file1.read()# Use this to read file content as a stream:
words = line.split()
for r in words:
    if not r in stop_words:
        appendFile = open('filteredtext.csv','a')
        appendFile.write(" "+r)
        appendFile.close()

