from navigation import Navigation
from shipment import Shipment
from transport import Transport
from location import Location
import random as rand


"""
The problem presented:
Given a full, weighted graph G, X number of Transporters with Y capacity each, and each node of G
containing a Z amount of shipments for other nodes in G, determine the most efficient/fastest way
of satisfying all shipments.

Transports may start and end their jobs on ANY nodes.
The logic should implement the basic behaviour of the Shipment Computer module, which automatically
picks up and delivers shipments as the Transports move through their designated path.
"""

num_shipments = 16
names = ["Haura", "Endor", "Zadaa", "Zadaa I", "Zadaa II", "My Mixtape", "My Mixtape I", "Neptune", "Neptune I"]
locations = [Location(n) for n in names]
distances = [
	# "Haura", "Endor", "Zadaa", "Zadaa I", "Zadaa II", "My Mixtape", "My Mixtape I", "Neptune", "Neptune I"
	[0, 643, 1284, 1284, 1284, 1043, 1043, 1768, 1768],
	[0, 0, 888, 888, 888, 523, 523, 1370, 1370],
	[0, 0, 0, 59, 105, 399, 399, 492, 492],
	[0, 0, 0, 0, 50, 399, 399, 492, 492],
	[0, 0, 0, 0, 0, 399, 399, 492, 492],
	[0, 0, 0, 0, 0, 0, 79, 856, 856],
	[0, 0, 0, 0, 0, 0, 0, 856, 856],
	[0, 0, 0, 0, 0, 0, 0, 0, 71],
	[0, 0, 0, 0, 0, 0, 0, 0, 0]
]
nav = Navigation(locations, distances)
# For every location...
# for loc in locations:
# 	# ...add a set amount of shipments...
# 	for i in range(num_shipments):
# 		# ...that are to other random locations obviously.
# 		while True:
# 			dest = rand.choice(locations)
# 			if dest != loc:
# 				break
# 		starmap.create_shipment(loc, dest, rand.randint(30, 200))
#
# # Now, let's test some of the basic shipment handling
# # transports = [Transport('Zadaa') for _ in range(3)]
# tran = Transport('Zadaa')
# tran.relocate('Haura')
# # tran.add_shipment()
# DONE figure out how to add shipments to graph???
# TODO rework the entire logic structure, this thing isn't going to work in current state, ever
# TODO figure out a proper way of representing the data
#  is a graph the only way possible? maybe just use it for baseline navigation and distance finder
# TODO study and replicate Shipment Computer module behavior
