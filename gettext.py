import httplib

conn = httplib.HTTPConnection('admin.freebird.prototyping.bbc.co.uk')
conn.request("GET", '/recipes/32.json')
r1 = conn.getresponse()
# print r1.status
body = r1.read()
# print body
import json
bodyJson = json.loads(body)
for item in bodyJson['items']:


	article_id = item['id']


	conn = httplib.HTTPConnection('admin.freebird.prototyping.bbc.co.uk')
	conn.request("GET", '/creative_works/' + article_id + '.json')
	r1 = conn.getresponse()
	# print r1.status
	body = r1.read()
	# print body
	import json
	bodyJson = json.loads(body)

	article_text = bodyJson['metadata']['http://schema.org/text']

	file = open('Examples/Text_bodies/' + article_id + ".txt", 'w')
	file.write(article_text.encode('utf8'))
	file.close