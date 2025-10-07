class car:
    def __init__(self, brand ,model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def start():
        print("car is starting")
    
    def stop():
        print("car is stopped")
        
class mustang(car):
    def start(self):
        print(f"{self.brand} {self.model} roars to life with a powerful engine!")
    
    def stop(self):
        print(f"{self.brand} {self.model} comes to a smooth halt.")
    
m = mustang("Ford", "Mustang GT", 2024)

m.start()
m.stop()
