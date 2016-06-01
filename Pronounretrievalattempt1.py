# -*- coding: utf-8 -*-
file = open('Examples/Guardian.txt')
source = file.read()
pronouns = ["i", "my", "me", "mine", "we", "us", "our", "ours"] 

count = 0
words = source.split ()
for word in words:
    if word.lower() in pronouns:
    	count += 1
    	# print word

print count
