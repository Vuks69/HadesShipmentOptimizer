class Shipment:
	value: int

	def __init__(self, destination, value: int = None):
		self.destination = destination
		if value is None:
			self.value = 0
		else:
			self.value = value
