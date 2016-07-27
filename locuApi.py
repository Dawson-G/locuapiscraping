import urllib2
import json
import locuApiKey

url = 'https://api.locu.com/v1_0/venue/search/?name=restaurant&locality=Chicago&api_key=' + locuApiKey.apiKey
json_obj = urllib2.urlopen(url)

data = json.load(json_obj)

for item in data['objects']:
    print item, "\n"