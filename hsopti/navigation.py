import networkx as nx
from location import Location


class Navigation:
	worldmap: nx.Graph

	def __init__(self, locations: [Location], distances: [[int]]):
		self.worldmap = nx.Graph()
		for i in range(len(locations)):
			for j in range(i + 1, len(locations)):
				self.worldmap.add_edge(locations[i], locations[j], distance=distances[i][j])

	def get_location_by_name(self, name: str):
		for n in self.worldmap.nodes:
			if n.name == name:
				return n

	def get_distance(self, place1: Location, place2: Location) -> int:
		return self.worldmap.get_edge_data(place1, place2)['distance']

	def get_path_length(self, pathlist: [Location]) -> int:
		return sum([self.get_distance(pathlist[i], pathlist[i+1]) for i in range(len(pathlist) - 1)])
