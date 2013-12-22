#!/usr/bin/python

'''
   This program is build to keep files updated from a list of links.

   Author: Breno Arosa
   Date: 12/2013
   Email: brenoarosa@hotmail.com

'''


from src import updateLib
from src import urlRead
from src import default

URL_FILE = 'urls.conf'

errors = 0
new = 0
updated = 0
maintained = 0

try:
  urls = urlRead.Urls(URL_FILE)
except IOError:
  print ("Fatal error!")
  print ("Missing url file: " + URL_FILE)
  print ("Restoring default file!")
  default.restore()
  exit(1)

if not urls.urlList:
  print ("Add links to: "+URL_FILE)
  exit(2)
  
for url in urls.urlList:
  up = updateLib.updateFile(url)
  up.connect()

  errors += up.errors
  new += up.new
  updated += up.updated
  maintained += up.maintained

print (str(errors)+" Access errors!")
print (str(new)+" new, "+str(updated)+ " updated, "+str(maintained)+" maintained!")
exit(0)
