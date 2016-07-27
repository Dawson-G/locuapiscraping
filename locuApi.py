import urllib2
import json
import locuApiKey

searchFor = "name=Food&locality=Chicago"
    
def locu_search(query):
    searchFor = query.replace(' ', '%20')
    url = "https://api.locu.com/v1_0/venue/search/?api_key=" + locuApiKey.apiKey + "&" + searchFor
    json_obj = urllib2.urlopen(url)
    
    data = json.load(json_obj)
    
    returnData = data['objects']
    
    return returnData
        
        
for item in locu_search(searchFor):
    print item['name'], item['website_url'], "\n"