import sys
import time
import json
import requests

class Geocoder():
    def __init__(self,geocoderName,addresses,apiKey=None):
        self.geocoderName = geocoderName
        self.addresses = addresses
        self.apiKey = apiKey
        
        
    def getGeocoderClass(self):
        geocoders = {"Google":GoogleMapsGeocoder(self.apiKey),"OSM":OpenStreetMapsGeocoder()} #add to this dict for each geocoder class
        return geocoders[self.geocoderName]

    def geocodeAddresses(self):
        results = []
        gc = self.getGeocoderClass()
        #params = gc.urlParameters()
        for address in self.addresses:
            time.sleep(0.1)
            coordinates = gc.geocodeAddress(address)
            results.append(coordinates)
        return results

            
class GoogleMapsGeocoder():
    def __init__(self,apiKey):
        self.url = "https://maps.googleapis.com/maps/api/geocode/json"
        self.apiKey = apiKey

    def urlParameters(self,address):
        return {"key": self.apiKey, "address": address}

    def geocodeAddress(self,address):
        connection = requests.get(self.url,self.urlParameters(address))
        connection.raise_for_status()
        try:
            data = connection.json()
            coordinates = data['results'][0]['geometry']['location']
            result = {"lat": coordinates['lat'],"long": coordinates['lng']}
        except: 
            print "Unable to geocode address: " + address
            result = None

        return result


class OpenStreetMapsGeocoder():
    def __init__(self):
        from geopy.geocoders import Nominatim
        self.gc = Nominatim()
    def geocodeAddress(self,address):
        data  = self.gc.geocode(address)
        try:
            result = ({"lat": data.latitude,"long": data.longitude})
        except:
            print "Unable to geocode address: " + address
            result = None
        return result

if __name__ == '__main__':
    gc = Geocoder("OSM",["30 roehampton court","ejrhojhnf","125 anvil street, kitchener, ontario"],'AIzaSyCZtmjtWfEWusp91YjMfR0mDprx_4PK9fo')
    print gc.geocodeAddresses()

