from shipment import Shipment
from transport import Transport


class Location:
	name: str
	shipments: [Shipment]
	stationed_ships: [Transport]

	def __init__(self, name, shipments=None, stationed_ships=None):
		self.name = name
		self.shipments = shipments or []
		self.stationed_ships = stationed_ships or []

	def add_shipment(self, to_add: Shipment):
		self.shipments.append(to_add)

	def bulk_add_shipments(self, to_add: [Shipment]):
		for ta in to_add:
			self.add_shipment(ta)

	def remove_shipment(self, to_remove: Shipment):
		self.shipments.remove(to_remove)

	def bulk_remove_shipments(self, to_remove: [Shipment]):
		for tr in to_remove:
			self.remove_shipment(tr)

	def get_shipments_to_next_loc(self, dest) -> [Shipment]:
		return [s for s in self.shipments if s.destination == dest]
