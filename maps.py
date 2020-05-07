import googlemaps
import requests
from datetime import datetime

url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input==DON%20HEIDA%20DAIRY%20&inputtype=textquery&fields=formatted_address,name&key=AIzaSyCD8h-VIhR-0m17rYy8WmbWhs-XN50Ft7s'

gmaps = requests.get(url)

resp_json = gmaps.json()

print(resp_json)
