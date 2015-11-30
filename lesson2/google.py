import urllib2
import json

s = 'https://query.yahooapis.com/v1/public/yql?q=select+*+from+yahoo.finance.xchange+where+pair+=+%22RUBUSD,RUBEUR%22&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback='
u = urllib2.urlopen(s)
data = u.read()
parsed_data = json.loads(data)

for n in parsed_data["query"]["results"]['rate']:
    print n["Name"]

print parsed_data