from multiprocessing import Pool, Manager


class WarehouseManager:
    def __init__(self):
        managers = Manager()
        self.data = managers.dict()

    def process_request(self, request):
        for i in request:
            product_name, action, quantity = i
            if action == 'receipt':
                if product_name in self.data:
                    self.data[product_name] += quantity
                else:
                    self.data[product_name] = quantity
            elif action == 'shipment':
                if product_name in self.data and self.data[product_name] >= quantity:
                    self.data[product_name] -= quantity

    def run(self, request):
        with Pool(processes=2) as pool:
            pool.map(self.process_request, [request])


if __name__ == "__main__":
    manager = WarehouseManager()

    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]

    manager.run(requests)
    print(manager.data)
