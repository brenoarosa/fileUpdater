#!/usr/bin/python

try:
# for python 3
  from urllib.request import urlopen
  from urllib.error import URLError
except ImportError:
#for python 2
  from urllib2 import urlopen
  from urllib2 import URLError

import os.path
import string
import random
import filecmp

def randomString(size=8, chars=string.ascii_letters + string.digits):
  return ''.join(random.choice(chars) for x in range(size))
	

class updateFile:
  #This class keep a file from a link updated
  '''
  url => url of the file
  listUrl => split url in a list to take the name of the file
  item => name of the file
  rndItem => name of temp file
  '''
  
  errors = 0
  updated = 0
  maintained = 0
  new = 0

  def __init__(self, url):
    self.url = url
    self.listUrl = self.url.split("/")
    self.item = self.listUrl[-1] 

  def connect(self):
    print ("Trying acess to: " + self.url)
    try:
      f = urlopen(self.url)

    except URLError:
      print ("Unable to acess: " + self.url)
      self.errors += 1
      return(URLError)

    print ("Downloading...")
    data = f.read()

    if os.path.isfile(self.item):
      self.rndItem = self.item + "." + randomString()
      with open(self.rndItem, "wb") as arquivo:
        arquivo.write(data)
      print ("Download Completed.")

      if filecmp.cmp(self.item, self.rndItem):
        print (self.item+" is already the newest version.")
        os.remove(self.rndItem)
        self.maintained += 1

      else:
        print ("Overwriting "+ self.item)
        os.remove(self.item)
        os.rename(self.rndItem, self.item)
        self.updated += 1

    else:
      with open(self.item, "wb") as arquivo:
        arquivo.write(data)
      print ("Download completed.")
      self.new += 1
  
    return(0)
