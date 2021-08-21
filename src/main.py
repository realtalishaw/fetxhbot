#!/usr/bin/python3
"""Queen Node Control Center"""
from DUE import due
from airport.arrivals import arrivals


def start(urls):
    due(urls)


urls = [
    'abc.com', "def.com", 'ghi.com', 'jkl.com', 'apple.com', 'google.com',
    'batman.com', 'ebay.com', "geeks.com", "apples.com", "barbie.com",
    "replit.com", "amazon.com"
]

start(urls)
