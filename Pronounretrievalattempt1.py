# -*- coding: utf-8 -*-
import glob
import re

folders = ["Non-Opinion", "Opinion"]
for folder in folders:
	print ""
	print folder
	countopinion = 0

	filenames = glob.glob('Examples/' + folder + '/*.txt')
	for filename in filenames:

		file = open(filename)
		source = file.read() 
		sourceWithoutQuotes = re.sub(r'“(.*?)”', "", source)
		sourceWithoutQuotes = re.sub(r'[‘“](.*?)[”’\n]', "", sourceWithoutQuotes)

		# print filename
		if filename == "Examples/Non-Opinion/MEN - Shoplifter.txt":
			print sourceWithoutQuotes
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

		print str(count) + " " + str(format(pronounperword, '.2f')) + " " + filename.replace('Examples/' + folder + "/", '')
	print float(countopinion)/float(len(filenames)) * 100
