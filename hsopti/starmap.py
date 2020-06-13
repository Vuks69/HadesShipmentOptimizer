import networkx as nx
from shipment import Shipment


class Starmap:
	star_map: nx.Graph

	def __init__(self, locations: [str], distances: [[int]]):
		self.star_map = nx.Graph()
		# Generate the full starmap
		self.star_map.add_nodes_from(locations, shipments=[])
		# And add all the connections along with distances
		for i in range(len(locations)):
			for j in range(i + 1, len(locations)):
				self.star_map.add_edge(locations[i], locations[j], distance=distances[i][j])

	def add_shipment(self, location: str, shipment: Shipment) -> None:
		self.star_map.nodes[location]['shipments'].append(shipment)

	def create_shipment(self, src: str, dst: str, val: int = None, amount: int = 1) -> None:
		if amount <= 0:
			raise ValueError('Amount of shipments to add must be 1 or higher.')
		for _ in range(amount):
			self.star_map.nodes[src]['shipments'].append(Shipment(dst, val))

	# def remove_shipment(self, location, to_remove: Shipment):
	# 	self.star_map[location]['shipments'].remove(to_remove)

	def get_distance(self, place1, place2) -> int:
		return self.star_map.get_edge_data(place1, place2)['distance']

	def get_path_length(self, pathlist: [str]) -> int:
		return sum([self.get_distance(pathlist[i], pathlist[i+1]) for i in range(len(pathlist) - 1)])


# At this point we have a complete, weighed graph representing the Yellow Star map, with all planets and moons.
# TODO figure out how to add shipments to graph???
# TODO figure out a proper way of representing the data
#  is a graph the only way possible? maybe just use it for baseline navigation and distance finder
# TODO find an algorithm to get efficient paths
#  3 ships with 5 max cargo each, every shipment weighs 1, find most efficient way to distribute all shipments
#  to where they belong. most efficient = least total distance OR least total paths taken
# TODO study and replicate Shipment Computer module behavior

