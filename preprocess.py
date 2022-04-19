import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
import ast
import re
from functools import reduce
remove_urls = lambda str: re.sub(r"http\S+", '',str)
remove_special_chars = lambda str: re.sub(r'[`\-=~!#$%^&*()+\[\]{};\'\\:"|</<>?]',' ',str)
tokenize = lambda str: word_tokenize(remove_special_chars("".join(i if 31 < ord(i) < 127 else " " for i in remove_urls(str))))
no_mentions = lambda ls : re.sub(' +',' ',reduce (lambda x,y: y+" " if len(x)==0 else x[:-2]+'<USER> ' if x.strip()[-1] == '@' else x+" "+y+" ",ls,"")).strip()
clean_tweet = lambda tweet: no_mentions(tokenize(tweet))