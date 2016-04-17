import urllib, urllib2, json

response = urllib2.urlopen('http://openstates.org/api/v1/bills/?apikey=5fb9eb7685334e23b35e355750024a30&state=mo&fields=sponsors,title').read()

data = json.loads(response)

for bill in data:
    encoded_bill_id = urllib.unquote(bill['sponsors'][0]['name']).encode('utf-8')
    encoded_bill_id2 = urllib.unquote(bill['title']).encode('utf-8')
    print encoded_bill_id, encoded_bill_id2
