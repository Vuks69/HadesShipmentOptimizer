from location import Location


class Shipment:
	destination: Location
	value: int

	def __init__(self, destination: Location, value: int = None):
		self.destination = destination
		if value is None:
			self.value = 0
		else:
			self.value = value
