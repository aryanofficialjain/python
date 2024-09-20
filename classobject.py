class Car: 
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model

    def fullname(self):
        return f"{self.brand} {self.__model}"
    
    def fuel_type(self):
        return " Petrol Diseal"
    
    @staticmethod
    def description(): 
        return "This is a car description cannot be accessed by Object"
    
    @property
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"  


electriccar = ElectricCar("Tesla","models s", "85KWh");
safari = Car("Tata", "Safari")
# safari.model = "City";
print(safari.model);
print(Car.description());
print(isinstance(electriccar ,Car));
print(isinstance(electriccar ,ElectricCar));





# my_car = Car("Bugatti", "Chiron");
# print(my_car.brand);        
# print(my_car.model);        
# print(my_car.fullname());        
        