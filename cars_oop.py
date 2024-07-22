class Cars:

    def __init__(self, producer: str, brand: str, gas_per_hundred_km: float, date_of_issue: int = 2020):
        self.date_of_issue = date_of_issue
        self.producer = producer.title()
        self.brand = brand.title()
        self.mileage = 0
        self.gas_consumption = gas_per_hundred_km

    def __str__(self) -> str:
        return f'<{self.brand}>'
        
    __repr__ = __str__


car1 = Cars(date_of_issue=2010, producer='China', brand='Chery',
            gas_per_hundred_km=8.916)
car1.mileage = 10000

car2 = Cars(date_of_issue=2001, producer='USA', brand='Jeep',
            gas_per_hundred_km=12.452)
car2.mileage = 12300

print(car2.__dict__)
print(car1.__dict__)
