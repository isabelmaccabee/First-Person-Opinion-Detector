# -*- coding: utf-8 -*-
import os

folders = ["Non-Opinion", "Opinion"]
for folder in folders:
	print ""
	print folder

	filenames = os.listdir('Examples/' + folder)
	for filename in filenames:

		file = open('Examples/' + folder + "/" + filename)
		source = file.read()
		pronouns = ["i", "my", "me", "mine", "we", "us", "our", "ours"] 

		count = 0
		words = source.split ()
		for word in words:
		    if word.lower() in pronouns:
		    	count += 1
		    	# print word

		pronounperword = float(count/float(len(words)))

		print str(count) + " " + str(format(pronounperword, '.2f')) + " " + filename