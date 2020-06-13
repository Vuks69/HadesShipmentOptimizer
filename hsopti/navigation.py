import networkx as nx
import random
from location import Location


class Navigation:
	worldmap: nx.Graph

	def __init__(self, locations: [Location], distances: [[int]]):
		self.worldmap = nx.Graph()
		for i in range(len(locations)):
			for j in range(i + 1, len(locations)):
				self.worldmap.add_edge(locations[i], locations[j], distance=distances[i][j])

	def generate_random_path(self, max_hops=15):
		locations = self.worldmap.nodes
		last = random.choice(locations)
		path = [last]
		current: Location
		for _ in range(max_hops):
			while True:
				current = random.choice(locations)
				if current != last:
					break
			path.append(current)
			last = current
		return path

	def location(self, name: str) -> Location:
		for n in self.worldmap:
			if n.name == name:
				return n

	def get_distance(self, place1: Location, place2: Location) -> int:
		if place1 == place2:
			return 0
		return self.worldmap.get_edge_data(place1, place2)['distance']

	def get_path_length(self, path: [Location]) -> int:
		if len(path) < 2:
			raise ValueError("Path must be of length 2 or more.")
		return sum([self.get_distance(path[i], path[i + 1]) for i in range(len(path) - 1)])
