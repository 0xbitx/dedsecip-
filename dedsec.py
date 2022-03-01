import argparse
import requests, json
import sys
from sys import argv
import os

parser = argparse.ArgumentParser()

parser.add_argument ("-t", help= "target/IP address", type=str, dest='target', required=True )

args = parser.parse_args()

green = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'

print (green+bold+"""

8888b.  888888 8888b.  .dP"Y8 888888  dP""b8    
 8I  Yb 88__    8I  Yb `Ybo." 88__   dP   `"         
 8I  dY 88""    8I  dY o.`Y8b 88""   Yb             
8888Y"  888888 8888Y"  8bodP' 888888  YboodP    
"""+green)
print (green+bold+"         CODED BY 0XBIT GUY \n"+clear)

ip = args.target

api = "http://ip-api.com/json/"

try:
        data = requests.get(api+ip).json()
        sys.stdout.flush()
        a = green+bold+"[*]"
        b = green+bold+"[*]"
        print (a, "[Victim]:", data['query'])
        print (b, "[ISP]:", data['isp'])
        print (a, "[Organisation]:", data['org'])
        print (b, "[City]:", data['city'])
        print (a, "[Region]:", data['region'])
        print (b, "[Longitude]:", data['lon'])
        print (a, "[Latitude]:", data['lat'])
        print (b, "[Time zone]:", data['timezone'])
        print (a, "[Zip code]:", data['zip'])
       
except KeyboardInterrupt:
        print ('Terminating'+green)
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
        print (green+"[~]"+" check your internet connection!"+clear)
sys.exit(1)
