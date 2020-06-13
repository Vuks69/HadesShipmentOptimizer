from shipment import Shipment


class Transport:
    max_cargo: int
    cargo: [Shipment]
    location: str

    def __init__(self, location: str, max_cargo: int = 5, cargo: [Shipment] = None):
        self.location = location
        self.max_cargo = max_cargo
        if cargo is None:
            self.cargo = []

    def relocate(self, to_where: str) -> (int, int):
        self.location = to_where
        return self.check_and_delete_shipments(to_where)

    def add_shipment(self, shipment: Shipment) -> None:
        self.cargo.append(shipment)

    def create_shipment(self, dst: str, val: int = None, amount: int = 1) -> None:
        if amount <= 0:
            raise ValueError('Amount of shipments to add must be 1 or higher.')
        for _ in range(amount):
            self.cargo.append(Shipment(dst, val))

    def check_and_delete_shipments(self, location: str) -> (int, int):
        to_delete = [s for s in self.cargo if s.destination == location]
        value = 0
        deleted = 0
        for td in to_delete:
            value += td.value or 0
            deleted += 1
            self.cargo.remove(td)
        return deleted, value
