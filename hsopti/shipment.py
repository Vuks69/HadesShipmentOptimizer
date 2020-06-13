class Shipment:
	destination: str
	value: int

	def __init__(self, destination: str, value: int = None):
		self.destination = destination
		if value is None:
			self.value = 1
		else:
			self.value = value
