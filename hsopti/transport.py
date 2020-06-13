from shipment import Shipment


class Transport:
    max_cargo: int
    cargo: [Shipment]

    def __init__(self, max_cargo: int = 5, cargo: [Shipment] = None):
        self.max_cargo = max_cargo
        self.cargo = cargo or []

    def load_shipment(self, shipment: Shipment) -> bool:
        if len(self.cargo) < 5:
            self.cargo.append(shipment)
            return True
        else:
            return False

    # def create_shipment(self, dst: Location, val: int = None, amount: int = 1) -> None:
    #     if amount <= 0:
    #         raise ValueError('Amount of shipments to add must be 1 or higher.')
    #     for _ in range(amount):
    #         self.add_shipment(Shipment(dst, val))

    # def check_and_delete_shipments(self, location: str) -> (int, int):
    #     to_delete = [s for s in self.cargo if s.destination == location]
    #     value = 0
    #     deleted = 0
    #     for td in to_delete:
    #         value += td.value
    #         deleted += 1
    #         self.cargo.remove(td)
    #     return deleted, value
