from location import Location


class ShipmentComputer:
	"""
	If you send a ship with a computer to planets A, B, C and D, at planet A it'll pick up as much as it can for B,
	then C if there are any remaining shipments and cargo space, etc.

	It can get a bit inefficient if, for example, you fly to planet A, then planet Z on the other side of your system,
	then to moon A I. If there are no shipments from A to Z, your ship in A could fill up with shipments to A I, fly to
	Z, have no space to pick up any of the high-paying shipments, and fly back to A I to deliver the shipments from A.
	"""
	def analyze_path(self, path: [Location]) -> int:
		pass
