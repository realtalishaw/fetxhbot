#!/usr/bin/python3
"""Creates WorkerIDs for incoming URLS and assigns them to appropriate Node"""
from airport.departures import boardingPass
passes = {}

def assignWorker(urls):
  print("Assigning Worker ID:")
  for url in urls:
    workerId = hash(url) % 3
    passes.setdefault(workerId, []).append(url)
    #if workerId not in passes:
      #passes[workerId] = list()
    #passes[workerId].extend(url)
  print(passes)
  airportTicket(passes)


def airportTicket(workerId):
  print("Sending to Airport")
  boardingPass(workerId)

  