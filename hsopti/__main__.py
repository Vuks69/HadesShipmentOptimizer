from starmap import Starmap
from shipment import Shipment
from transport import Transport
import random as rand

num_shipments = 16
locations = ["Haura", "Endor", "Zadaa", "Zadaa I", "Zadaa II", "My Mixtape", "My Mixtape I", "Neptune", "Neptune I"]
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
starmap = Starmap(locations, distances)
# For every location...
for loc in locations:
	# ...add a set amount of shipments...
	for i in range(num_shipments):
		# ...that are to other random locations obviously.
		while True:
			dest = rand.choice(locations)
			if dest != loc:
				break
		starmap.create_shipment(loc, dest)

# Now, let's test some of the basic shipment handling
# transports = [Transport('Zadaa') for _ in range(3)]
tran = Transport('Zadaa')
