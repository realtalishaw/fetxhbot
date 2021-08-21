#!/usr/bin/python3
"""Duplicate URL Eliminator"""
from workerID import assignWorker
from bloomfilter import BloomFilter

n = 100 #number of items to add
p = 0.001 #false positive probability

bloom = BloomFilter(n, p)

def due(urls):
  print("Testing for Duplicate URLS")
  for url in urls:
    if bloom.check(url):
      urls.remove(url)
      print("Duplicated Detected: " + url)
    else:
      bloom.add(url)
      print("New URL added to filter: " + url)
  return assignWorker(urls)
