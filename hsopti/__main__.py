from location import Location
from navigation import Navigation

"""
The problem presented:
Given a full, weighted graph G, X number of Transporters with Y capacity each, and each node of G
containing a Z amount of shipments for other nodes in G, determine the most efficient/fastest way
of satisfying all shipments.

Transports may start and end their jobs on ANY nodes.
The logic should implement the basic behaviour of the Shipment Computer module, which automatically
picks up and delivers shipments as the Transports move through their designated path.
"""
print('Creating navmap weighted graph...')
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
print('Navmap created')
print('Initializing shipments...')
# TODO prepare some shipments for testing purposes - use random with a set seed to analyse future results
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
print('Shipments initialized')
print('Initializing Transport ships...')
# TODO spawn some transports - one should be good enough for early testing.
#  not sure how to deal with 3 ships working simultaneously, but hey, that's a job for future me working on SComputer
print('Transports initialized')
print('Firing up the Shipment Computer...')
# TODO berate past me for starting this project, also implement basic SComputer logic, path testing
#  and some way to return an optimized path
# note: trying to set a full, 15-node path might not even work - I might have to resort to manually imputting the path
# right after the transport passes a node and does its shipment magic
# bonus TODO add an approximation of expected hydrogen costs for all the hauling around
print('Shipment Computer blew up')

