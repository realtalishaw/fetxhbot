#!/usr/bin/python3
"""Welcome to the Queen Node Airport, with service to all other nodes via API"""
from node1.airport import arrivals

def boardingPass(workerId):
  for n in range(0, 3):
    passengers = workerId[n]
    print("Now Boarding Terminal", n, workerId[n])
    if n == 1:
      terminal1(passengers)
    if n == 0:
      terminal0(passengers)

def terminal1(passengers):
  print("passengers departed from terminal 1 to worker 1:", passengers)
  arrivals(passengers)

def terminal0(passengers):
  print("passengers departed from terminal 0 to worker 0:", passengers)
