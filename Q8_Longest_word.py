#8.Write a python program to find the longest words.

import re

t1="hello good morning"
word=r'\w+'
sub=re.findall(word,t1)
max_word=max(sub,key=len)
print(max_word)
