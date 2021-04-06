class Vehicle:
    available = ["Lambo", "Ferrari", "Opel"]

    def __init__(self, wheel, brand, CV):
        self.wheel = wheel
        self.brand = brand
        self.CV = CV
        print("Vehicle created!")

    def __str__(self): #si pones print("una clase") te va a dar la localizacion de la clase, pero esto lo convierte en string y lo imprime
        return "The wheel is: " + self.wheel + "\n" + "The brand is: " + self.brand + "\n" + "The CV are: " + str(self.CV)

    @staticmethod
    def print_seq(cls):
        return "The wheel is: " + cls.wheel + "\n" + "The brand is: " + cls.brand + "\n" + "The CV are: " + str(cls.CV)

    def calculate_price(self):
        if self.brand == "Ferrari":
            return "It cost a lot, buy me another"
        else:
            return "My " + self.brand + " is cheap but I love it <3"