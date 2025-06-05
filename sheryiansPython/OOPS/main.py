class Factory:
    def __init__(self, materials, zip, pockets):
        self.material = materials
        self.zip = zip
        self.pockets = pockets


    def show(self):
        print(f"Materials is: {self.material}\nTotal zip are: {self.zip}\nTotal pockets are: {self.pockets} ")    


obj1 = Factory("Leather", 3,5)
obj2 = Factory("Cotton", 3,5)
obj3 = Factory("Nylon", 3,5)


obj1.show()
obj2.show()
obj3.show()