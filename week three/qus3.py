class car:
    def __init__(self,make):
        self.make=make
    def get_make(self):
        return self.make
    
c1=car("toyota")
print(c1.get_make())