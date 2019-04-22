import sys
from suds import null, WebFault
from suds.client import Client
import logging

file = open('apikey')
x = file.read().split("\n")
file.close()
print(x)
username = x[0]
apiKey = x[1]
url = 'http://flightxml.flightaware.com/soap/FlightXML2/wsdl'

logging.basicConfig(level=logging.INFO)
api = Client(url,username=username, password=apiKey)
print(api)

# Get the weather
result = api.service.Metar('KAUS')
print(result)

# Get the flights enroute
result = api.service.FlightInfo("N128AM",3)
flights = result['flights']

print("Aircraft en route to KSMO:")
for flight in flights:
    print("%s (%s) \t%s (%s)" % ( flight['ident'], flight['aircrafttype'],
                                  flight['originName'], flight['origin']))
