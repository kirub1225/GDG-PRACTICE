class vehicle:
    def __init__(self,brand,year):
        self.brand= brand
        self.year=year
    def info(self):
        print(self.brand)
        print(self.year)
class car(vehicle):
     def __init__ (self,brand,year,model):
         super().__init__(brand,year)
         self.model=model
     def  info(self):
          super().info()
          print(self.model)
v1=vehicle("Tesla",2010)
c1=car("Tesla",2010,"model3")
v1.info()
c1.info()

    
         
     
    

    
