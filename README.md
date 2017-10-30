## Geocoding

This repository contains a general purpose geocoder (geocoder.py) which can call various geocoders (Google Maps, OSM, etc) and return a lat/long JSON object.
To start, simply initialize Geocoder class: gc = Geocoder("GeocoderName",[list of addresses],'API Key'), where GeocoderName is "Google" or "OSM". Note that some geocoders don't need an API Key (such as OSM) and this field can be left blank)
And return a list of coordinates in the same order as entered: gc.geocodeAddresses()

### TODO
* add more geocoders such as Mapbox, Mapzen, Geocodio, etc
* add logging, better error handling
* add a spreadsheet with an address column and script to geocode the addresses
