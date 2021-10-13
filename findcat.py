from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import os
import webbrowser

os.chdir = input("enter directory: ")
catImage = Image.open(input("enter image name: "))


catExifData = catImage._getexif()
catGPSData = catExifData[34853]

lat = catGPSData[2]
lon = catGPSData[4]

def dmsToDecimal(degTriple):
    return degTriple[0] + degTriple[1]/60.0 + degTriple[2]/3600.0

latDec = dmsToDecimal(lat)
lonDec = dmsToDecimal(lon)

if catGPSData[1] == 'S':
    latDec = -latDec

if catGPSData[3] == 'W':
    lonDec = -lonDec

print("lat: ",latDec)
print("lon: ",lonDec)

print(latDec," , ",lonDec)

locString=str(latDec)+','+str(lonDec)
mapURL = 'https://www.google.com/maps/place/' + locString
webbrowser.open(mapURL)
