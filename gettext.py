import httplib
conn = httplib.HTTPConnection('admin.freebird.prototyping.bbc.co.uk')
conn.request("GET", "/creative_works/7869347.json")
r1 = conn.getresponse()
# print r1.status
body = r1.read()
# print body
import json
bodyJson = json.loads(body)
print bodyJson['id']
print bodyJson['metadata']['http://schema.org/text']