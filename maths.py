import urllib2
import pylab as pl
import numpy as np
#import sys
#from bs4 import BeautifulSoup
#from pytagcloud import create_tag_image, make_tags
#from pytagcloud.lang.counter import get_tag_counts
import os
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.corpus import words
from nltk.corpus import stopwords

#content=urllib2.urlopen("/home/rohan/Desktop/CompleteSearch.html")
e=open("html3.txt","r")
f=open("xample.txt","w+")
g=open("xample2.txt","w+")
h=open("stopword.txt","r")
p=open("dictionary.txt","r")
btext={}
#sort={}
top_20={}
top_15={}
q=""
s=""
y=""
stop=stopwords.words('english')
#for i in soup.get_text():
    #print i
    #print "a"
#    for word in i.text.split():
#        f.write(word)
#        f.write(' ')
        #print "z"
        #print word
        #if word not in btext:
        #    btext[str(word)]=1
        #else:
        #    btext[str(word)]+=1
        #print "end"
        #print btext
#for i in btext.keys():
#    btext[i]/=3
#print btext
"""f.seek(0)"""
for line in e:
    for i in line:
        if (ord(i)==32 or i=='\n' or(ord(i)>=48 and ord(i)<=57)or(ord(i)>=65 and ord(i)<=90)or(ord(i)>=97 and ord(i)<=122)):
            g.write(i)
        else:
            g.write(' ')
g.seek(0)
a=[]
for word in h:
    if word not in a:
        a.append(word[:-1])
b=[]
for word in p:
    if word not in b:
        b.append(word[:-1])
#print a
for line in g:
    for w in line.split():
        if w.lower() not in a and w.lower() not in stop and w.lower() in b and len(w)>1:
            f.write(w.lower())
            f.write('\n')
f.seek(0)
for line in f:
    for i in line.split():
        if i not in btext:
            btext[i]=1
        else:
            btext[i]+=1
#print btext
#print "rohan"
sort=sorted(btext,key=btext.get,reverse=True)
for w in sort[:20]:
    top_20[w]=btext[w]
for w in sort[:15]:
    top_15[w]=btext[w]
top=sum(top_15.values())
print top
for w in top_15.keys():
    top_15[w]/=float(top)
print top_20
print top_15

x=np.arange(len(top_20))
pl.bar(x, top_20.values(), align='center', width=0.5)
pl.xticks(x, top_20.keys())
ymax=max(top_20.values())
pl.ylim(0, ymax+1)
pl.show()
x=np.arange(len(top_15))
pl.bar(x, top_15.values(), align='center', width=0.5)
pl.xticks(x, top_15.keys())
ymax=max(top_15.values())
pl.ylim(0, ymax+1)
pl.show()
f.seek(0)
for w in f:
	for i in w.split():
	    q+=w
	    q+=" "
wordcloud=WordCloud(font_path=None, width=400, height=200, margin=5, ranks_only=False, prefer_horizontal=0.9, mask=None, scale=1, max_words=200, stopwords=None, random_state=None, background_color='black', max_font_size=None).generate(q)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
e.close()
g.close()
f.close()
h.close()