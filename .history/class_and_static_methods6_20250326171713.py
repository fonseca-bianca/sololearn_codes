"""
The SportsCar class inherits from the class Car. The Car class
has the make and model attibutes.
1 - Define the SportsCar class and add a top_speed attribute 
to it.
"""

class SportsCar(Car):
    def __init__(self, make, model, top_speed):
        # self.make = make
        # self.model = model
    
        super().__init__(make,model)
        self.top_speed = top_speed