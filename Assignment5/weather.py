import requests
import time

def get_weather(z, token):
	address = "http://api.openweathermap.org/data/2.5/weather?zip=%s,%s&APPID=%s"
	resp = requests.post(address % (z, 'us', token))
	return resp.json()

z = '30060' # south campus zip
country = 'us'
key = '0812a639bbbbe34e3bac0e70bbd18218'

#address = "http://api.openweathermap.org/data/2.5/weather?zip=%s,%s&APPID=%s"
#address = address % (z, country, key)
#resp = requests.post(address)
#print(resp.json())

json = get_weather(z, key)
print("Name: " + json['name'])
print("Current temperature: %.2f F" % (json['main']['temp'] * (9/5) - 459.67))
print("Atmosphere pressure: " + str(json['main']['pressure']) + " hPa")
print("Wind Speed: " + str(json['wind']['speed']) + str(" mph"))
print("Wind Direction: " + str(json['wind']['deg']))
print("Time of report: " + str(time.ctime(json['dt'])))
print()
