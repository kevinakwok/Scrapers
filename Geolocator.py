#Limited by Google Map's daily limits.
#Removed some extra commas
#Changed Laura LA to Laura LN
#44 Laura Ln strangely returned an Arizonian address. had to redo it.


from googlemaps import GoogleMaps
import re
import csv
import xlwt
import time

api_key = 'ABQIAAAAfuy4dojnFhd2b4DGaIDdyBQgRrDPz5uMIWLTeW6L3RbWlsN7pRRrtNwHqXGSxUdjd2alpsI9JI_8Xw'

gmaps = GoogleMaps(api_key)

locations = csv.reader(open('Desktop/location2.csv', 'rU'), dialect =csv.excel_tab)
wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')

r = 0
for row in locations:
    address = 'XXX, New Haven, CT'
    first = re.search('^(.*),',row[0])
    address = re.sub('XXX',first.group(), address)
    lat, lng = gmaps.address_to_latlng(address)
    ws.write(r, 0, row[0])
    ws.write(r, 1, lat)
    ws.write(r, 2, lng)
    r = r +1
    #Needs a one secodn sleep to avoid Google Map's rate limit.
    time.sleep(1.0)


wb.save('completeGeoLocations3.csv')