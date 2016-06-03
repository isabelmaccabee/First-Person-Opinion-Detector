import httplib
conn = httplib.HTTPConnection('admin.freebird.prototyping.bbc.co.uk')
conn.request("GET", "/creative_works/7869347.json")
r1 = conn.getresponse()
# print r1.status
body = r1.read()
# print body
import json
bodyJson = json.loads(body)
article_id = bodyJson['id']
article_text = bodyJson['metadata']['http://schema.org/text']
# import os
# for os import rename, listdir
# # 	# os.rename(bodyJson['metadata']['http://schema.org/text'], bodyJson['id'])
# article_text
# f = open(article_text, 'w')
# f.write(article_text.encode('utf8'))
# f.close()

file = open(article_id + ".txt", 'w')
file.write(article_text.encode('utf8'))
file.close
# file = open(article_id + ".txt", 'w')
# file.write(article_text)
# file.close()