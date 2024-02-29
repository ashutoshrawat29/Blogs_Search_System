# import codecs
# import sys
# import csv
# import nltk
# nltk.download('stopwords')
# nltk.download('punkt')
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
# from nltk.stem import PorterStemmer
# from collections import Counter
# from num2words import num2words
# import os
# import string
# import numpy as np
# import copy
# import pandas as pd
# import pickle
# import re
# import math

# def convert_lower_case(data):
#     return np.char.lower(data)

# def remove_stop_words(data):
#     stop_words = stopwords.words('english')
#     words = word_tokenize(str(data))
#     new_text = ""
#     for w in words:
#         if w not in stop_words and len(w) > 1:
#             new_text = new_text + " " + w
#     return new_text

# def remove_punctuation(data):
#     symbols = "!\"#$%&()*+-./:;<=>?@[\]^_`{|}~\n"
#     for i in range(len(symbols)):
#         data = np.char.replace(data, symbols[i], ' ')
#         data = np.char.replace(data, "  ", " ")
#     data = np.char.replace(data, ',', '')
#     return data

# def remove_apostrophe(data):
#     return np.char.replace(data, "'", "")

# def stemming(data):
#     stemmer= PorterStemmer()
    
#     tokens = word_tokenize(str(data))
#     new_text = ""
#     for w in tokens:
#         new_text = new_text + " " + stemmer.stem(w)
#     return new_text

# def convert_numbers(data):
#     tokens = word_tokenize(str(data))
#     new_text = ""
#     for w in tokens:
#         try:
#             w = num2words(int(w))
#         except:
#             a = 0
#         new_text = new_text + " " + w
#     new_text = np.char.replace(new_text, "-", " ")
#     return new_text

# def preprocess(data):
#     data = convert_lower_case(data)
#     data = remove_punctuation(data) #remove comma seperately
#     data = remove_apostrophe(data)
#     data = remove_stop_words(data)
#     data = convert_numbers(data)
#     data = stemming(data)
#     data = remove_punctuation(data)
#     data = convert_numbers(data)
#     data = stemming(data) #needed again as we need to stem the words
#     data = remove_punctuation(data) #needed again as num2word is giving few hypens and commas fourty-one
#     data = remove_stop_words(data) #needed again as num2word is giving stop words 101 - one hundred and one
#     return data

# maxInt = sys.maxsize

# while True:
#     # decrease the maxInt value by factor 10 
#     # as long as the OverflowError occurs.

#     try:
#         csv.field_size_limit(maxInt)
#         break
#     except OverflowError:
#         maxInt = int(maxInt/10)
# blog_text=[]
# doc=[]
# index={}
# with codecs.open("./server/blogtext.csv",'r',encoding="utf8") as file:
#   csvreader = csv.reader(x.replace('\0', '') for x in file)
#   i=0
#   perc=0
#   print("start")
#   for row in csvreader:
#     i=i+1
#     perc=perc+1
#     if(perc==500):
#         print("10% more done")
#         perc=0
#     if(i==5000):
#         print("wait..")
#         break
#     doc.append(row)
#     blog_text.append(word_tokenize(str(preprocess(row[6].strip()))))
#     for token in blog_text[i-1]:
#         if token not in index:
#             index[token]=set()
#         index[token].add(i)
    
# print(len(blog_text))
# print(blog_text[23])
# print(doc[23])
# print(index['vapor'])
# print(len(index))

# def weights_norms(data):
#     vector={}
#     for i in index:
#         vector[i]=0
#     tf=Counter(data)   
#     norm=0
#     for i in tf:
#         if i in index:
#             df=len(index[i])
#             #idf
#             idf=math.log2(len(doc)/df)
#             #logtf
#             tf[i]=1+math.log2(tf[i])
#             tf[i]*=idf
#             vector[i]=tf[i]
#             #norm
#             norm+=(tf[i]**2)
#     return [vector,math.sqrt(norm)]

# #Scoring
# weight=[]
# for b in blog_text:
#     weight.append(weights_norms(b))

# #Similarity
# def cosine(q,d):
#     dot=0
#     for qv in q[0]:
#         dot+=d[0][qv]*q[0][qv]
#     angle=dot/(d[1]*q[1])
#     return angle

# def search(query):
#     analyzed_query = word_tokenize(str(preprocess(query)))
#     results=[index.get(token,set()) for token in analyzed_query]
#     documents_id = [doc_id-1 for doc_id in set.intersection(*results)]
#     query_vector=weights_norms(analyzed_query)
#     costhetas=[]
#     for ids in documents_id:
#         costhetas.append([ids,cosine(query_vector,weight[ids])])
#     return sorted(costhetas,key=lambda doc:doc[1],reverse=True)

# def vector_maker(d):
#     vector=[]
#     for w in d:
#         vector.append(d[w])
#     return vector

# #pseudo relevance feedback
# def queryoptimizer(query,reldoc_ids,nonreldoc_ids):
#     alpha=1
#     beta=0.75
#     gamma=0.25
#     mat_sum_rel=vector_maker(weight[reldoc_ids[0]][0])
#     for _id in reldoc_ids:
#         if(_id!=reldoc_ids[0]):
#             mat_sum_rel=np.add(mat_sum_rel,vector_maker(weight[_id][0]))
#     mat_sum_rel=np.divide(mat_sum_rel,len(reldoc_ids))
#     mat_sum_nonrel=vector_maker(weight[nonreldoc_ids[0]][0])
#     for _id in nonreldoc_ids:
#         if(_id!=nonreldoc_ids[0]):
#             mat_sum_nonrel=np.add(mat_sum_nonrel,vector_maker(weight[_id][0]))
#     mat_sum_nonrel=np.divide(mat_sum_nonrel,len(nonreldoc_ids))
#     qv=np.multiply(vector_maker(query[0]),alpha)
#     mat_sum_rel=np.multiply(mat_sum_rel,beta)
#     mat_sum_nonrel=np.multiply(mat_sum_nonrel,gamma)
#     q_opt=np.add(qv,np.subtract(mat_sum_rel,mat_sum_nonrel))

import codecs
import sys
import csv
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from collections import Counter
import num2words
from num2words import num2words

import numpy as np
import pandas as pd
import math

def convert_lower_case(data):
    return np.char.lower(data)

def remove_stop_words(data):
    stop_words = stopwords.words('english')
    words = word_tokenize(str(data))
    new_text = ""
    for w in words:
        if w not in stop_words and len(w) > 1:
            new_text = new_text + " " + w
    return new_text

def remove_punctuation(data):
    symbols = "!\"#$%&()*+-./:;<=>?@[\]^_`{|}~\n"
    for i in range(len(symbols)):
        data = np.char.replace(data, symbols[i], ' ')
        data = np.char.replace(data, "  ", " ")
    data = np.char.replace(data, ',', '')
    return data

def remove_apostrophe(data):
    return np.char.replace(data, "'", "")

def stemming(data):
    stemmer= PorterStemmer()
    
    tokens = word_tokenize(str(data))
    new_text = ""
    for w in tokens:
        new_text = new_text + " " + stemmer.stem(w)
    return new_text

def convert_numbers(data):
    tokens = word_tokenize(str(data))
    new_text = ""
    for w in tokens:
        try:
            w = num2words(int(w))
        except:
            a = 0
        new_text = new_text + " " + w
    new_text = np.char.replace(new_text, "-", " ")
    return new_text

def preprocess(data):
    data = convert_lower_case(data)
    data = remove_punctuation(data) #remove comma seperately
    data = remove_apostrophe(data)
    data = remove_stop_words(data)
    data = convert_numbers(data)
    data = stemming(data)
    data = remove_punctuation(data)
    data = convert_numbers(data)
    data = stemming(data) #needed again as we need to stem the words
    data = remove_punctuation(data) #needed again as num2word is giving few hypens and commas fourty-one
    data = remove_stop_words(data) #needed again as num2word is giving stop words 101 - one hundred and one
    return data

maxInt = sys.maxsize

while True:
    # decrease the maxInt value by factor 10 
    # as long as the OverflowError occurs.

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)
blog_text=[]
doc=[]
index={}
with codecs.open("./server/blogtext.csv",'r',encoding="utf8") as file:
  csvreader = csv.reader(x.replace('\0', '') for x in file)
  i=0
  perc=0
  print("start")
  for row in csvreader:
    i=i+1
    perc=perc+1
    if(perc==5000):
        print("10% more done")
        perc=0
    if(i==10000):
        print("wait..")
        break
    doc.append(row)
    blog_text.append(word_tokenize(str(preprocess(row[6].strip()))))
    for token in blog_text[i-1]:
        if token not in index:
            index[token]=set()
        index[token].add(i)
    
# print(len(blog_text))
# print(blog_text[23])
# print(doc[23])
# print(index)
# print(len(index))

def weights_norms(data):
    vector={}
    for i in index:
        vector[i]=0
    tf=Counter(data)   
    norm=0
    for i in tf:
        if i in index:
            df=len(index[i])
            #idf
            idf=math.log2(len(doc)/df)
            #logtf
            tf[i]=1+math.log2(tf[i])
            tf[i]*=idf
            vector[i]=tf[i]
            #norm
            norm+=(tf[i]**2)
    return [vector,math.sqrt(norm)]

#Scoring
weight=[]
for b in blog_text:
    weight.append(weights_norms(b))

#Similarity
def cosine(q,d):
    dot=0
    for qv in q[0]:
        dot+=d[0][qv]*q[0][qv]
    angle=dot/(d[1]*q[1])
    return angle

def search(query):
    analyzed_query = word_tokenize(str(preprocess(query)))
    results=[index.get(token,set()) for token in analyzed_query]
    documents_id = [doc_id-1 for doc_id in set.intersection(*results)]
    query_vector=weights_norms(analyzed_query)
    costhetas=[]
    for ids in documents_id:
        costhetas.append([ids,cosine(query_vector,weight[ids])])
    return sorted(costhetas,key=lambda doc:doc[1],reverse=True)

def vector_maker(d):
    vector=[]
    for w in d:
        vector.append(d[w])
    return vector

#pseudo relevance feedback
def queryoptimizer(query,reldoc_ids,nonreldoc_ids):
    alpha=1
    beta=0.75
    gamma=0.25
    mat_sum_rel=np.zeros(len(weight[0][0]))
    for _id in reldoc_ids:
        mat_sum_rel=np.add(mat_sum_rel,vector_maker(weight[_id][0]))
    if(len(reldoc_ids)!=0):
        mat_sum_rel=np.divide(mat_sum_rel,len(reldoc_ids))
    mat_sum_nonrel=np.zeros(len(weight[0][0]))
    for _id in nonreldoc_ids:
        mat_sum_nonrel=np.add(mat_sum_nonrel,vector_maker(weight[_id][0]))
    if(len(nonreldoc_ids)!=0):
        mat_sum_nonrel=np.divide(mat_sum_nonrel,len(nonreldoc_ids))
    qv=np.multiply(vector_maker(query[0]),alpha)
    mat_sum_rel=np.multiply(mat_sum_rel,beta)
    mat_sum_nonrel=np.multiply(mat_sum_nonrel,gamma)
    q_opt=np.add(qv,np.subtract(mat_sum_rel,mat_sum_nonrel))
    #now made optimized query vector and now converting it back
    u=0
    norm=0
    print(len(query[0]))
    print(len(index))
    for w in query[0]:
        query[0][w]=q_opt[u]
        norm+=q_opt[u]**2
        u+=1
    query[1]=math.sqrt(norm)
    new_results=[]
    for token in query[0]:
        if(query[0][token]!=0):
            new_results.append(index.get(token,set()))
    print(len(new_results))
    documents_id = [doc_id-1 for doc_id in set.union(*new_results)]
    costhetas=[]
    for ids in documents_id:
        costhetas.append([ids,cosine(query,weight[ids])])
    return sorted(costhetas,key=lambda doc:doc[1],reverse=True)

def queryoptimizer_fast(query,reldoc_ids,nonreldoc_ids,result_docs):
    alpha=1
    beta=0.75
    gamma=0.25
    mat_sum_rel=np.zeros(len(weight[0][0]))
    for _id in reldoc_ids:
        mat_sum_rel=np.add(mat_sum_rel,vector_maker(weight[_id][0]))
        print(mat_sum_rel)
    if(len(reldoc_ids)!=0):
        mat_sum_rel=np.divide(mat_sum_rel,len(reldoc_ids))
    mat_sum_nonrel=np.zeros(len(weight[0][0]))
    for _id in nonreldoc_ids:
        mat_sum_nonrel=np.add(mat_sum_nonrel,vector_maker(weight[_id][0]))
    if(len(nonreldoc_ids)!=0):
        mat_sum_nonrel=np.divide(mat_sum_nonrel,len(nonreldoc_ids))
    qv=np.multiply(vector_maker(query[0]),alpha)
    mat_sum_rel=np.multiply(mat_sum_rel,beta)
    mat_sum_nonrel=np.multiply(mat_sum_nonrel,gamma)
    q_opt=np.add(qv,np.subtract(mat_sum_rel,mat_sum_nonrel))
    #now made optimized query vector and now converting it back
    u=0
    norm=0
    print(len(query[0]))
    print(len(index))
    for w in query[0]:
        query[0][w]=q_opt[u]
        norm+=q_opt[u]**2
        u+=1
    query[1]=math.sqrt(norm)
    
    costhetas=[]
    for ids in result_docs:
        costhetas.append([ids[0],cosine(query,weight[ids[0]])])
    return sorted(costhetas,key=lambda doc:doc[1],reverse=True)

def rochchio(query,reldoc_ids,nonreldoc_ids,choice):
    analyzed_query = word_tokenize(str(preprocess(query)))
    query_vector=weights_norms(analyzed_query)
    if(choice==0):
        return queryoptimizer(query_vector,reldoc_ids,nonreldoc_ids)
    else:
        return queryoptimizer_fast(query_vector,reldoc_ids,nonreldoc_ids,search(query))

# print(search('answer this very tough question'))
# print(rochchio('answer this very tough question',[749,3687],[7476],1))


def doc_(query):
    result = []
    search__ = search(query)
    for x in search__:
        # print(x)
        result.append([doc[x[0]],x[0]])
    return result

def doc_feedback(query,reldoc_ids,nonreldoc_ids,choice):
    result = []
    search__ =rochchio(query,reldoc_ids,nonreldoc_ids,choice)
    for x in search__:
        # print(x)
        result.append([doc[x[0]],x[0]])
        
    return result


# print(doc[search('answer')[0][0]])
# print((weight[4880][0])*100)
# print(Counter(blog_text[3])['bomb'])

#583, 0.24419406311723063