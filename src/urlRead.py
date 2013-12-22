#!/usr/bin/python

class Urls:
  urlList = []

  def __init__(self, url_file):
    self.url_file = url_file
    try:
      f = open(self.url_file)
    except IOError:
      raise IOError("Missing url file: "+ self.url_file)

    for line in f:
      if (line[0] != '#') and (line[0] != '\n'):
        line = line[:-1]	#removes \n
        self.urlList.append(line)

    f.close()
