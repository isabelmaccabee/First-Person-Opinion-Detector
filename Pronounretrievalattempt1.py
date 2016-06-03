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
		sourceWithoutParagraphs = re.sub(r'\n', " ", source)
		# if filename == "Examples/Non-Opinion/MEN - Shoplifter.txt":
		# 	print sourceWithoutParagraphs
		sourceWithoutQuotes = re.sub(r'“(.*?)”', "", sourceWithoutParagraphs)
		sourceWithoutQuotes = re.sub(r'[‘“](.*?)[”’\n]', "", sourceWithoutQuotes)
		sourceWithoutQuotes = re.sub(r'"(.*?)"\s', "", sourceWithoutQuotes)
		sourceWithoutQuotes = re.sub(r'"(.*?)"', "", sourceWithoutQuotes)
		# print filename
		# if filename == "Examples/Non-Opinion/Vice - weed.txt":
		# 	print sourceWithoutQuotes
		pronouns = ["i", "my", "me", "mine", "we", "us", "our", "ours"] 

		count = 0
		words = re.split ('\W+', sourceWithoutQuotes)
		for word in words:
		    if word.lower() in pronouns:
		    	count += 1
		    	# if filename == "Examples/Non-Opinion/Vice - Female Hormones.txt":
		    	# 	# print word
		    	# 	count = 0

		pronounperword = float(count/float(len(words)))
		if pronounperword > 0.005:
			countopinion += 1
		# if count > 10:
		# 	countopinion += 1

		print str(count) + " " + str(format(pronounperword, '.3f')) + " " + filename.replace('Examples/' + folder + "/", '')
	print float(countopinion)/float(len(filenames)) * 100
