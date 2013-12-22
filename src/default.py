#!/usr/bin/pytho

import os
import shutil

def restore():
  atual = os.path.dirname(os.path.abspath(__file__)) 
  urlSrc = os.path.join(atual, 'default/urls.conf')
  
  urlDest = os.path.join(os.path.dirname(atual), 'urls.conf')
  
  print ("Copying from: "+urlSrc)
  print ("Copying to: "+urlDest)

  shutil.copyfile ( urlSrc , urlDest )
