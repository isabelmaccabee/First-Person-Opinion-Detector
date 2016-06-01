# -*- coding: utf-8 -*-
import os
import re

folders = ["Non-Opinion", "Opinion"]
for folder in folders:
	print ""
	print folder
	countopinion = 0

	filenames = os.listdir('Examples/' + folder)
	for filename in filenames:

		file = open('Examples/' + folder + "/" + filename)
		source = file.read() 
		# sourceWithoutQuotes = re.sub(r'“[^”]*”', "", source)
		sourceWithoutQuotes = re.sub(r'“(.*?)”', "", source)
		# if filename == "Politics Immigration article.txt":
		# 	print sourceWithoutQuotes
		# sourceWithoutQuotes = source.replace(/\"[^\"]*\"/, "")
		pronouns = ["i", "my", "me", "mine", "we", "us", "our", "ours"] 

		count = 0
		words = re.split ('\W+', sourceWithoutQuotes)
		for word in words:
		    if word.lower() in pronouns:
		    	count += 1
		    	# print word

		pronounperword = float(count/float(len(words)))
		if pronounperword > 0.02:
			countopinion += 1
		# if count > 10:
		# 	countopinion += 1

		print str(count) + " " + str(format(pronounperword, '.2f')) + " " + filename
	print float(countopinion)/float(len(filenames)) * 100