import urllib2
import json

api_key ='ohadsonascoqjasdpkqwmas'
url = 'https://api.openweathermap.org/data/2.5/weather?q=Nairobi'
json_obj = urllib2.urlopen(url)
data = json.load(json_obj)

print (data)

