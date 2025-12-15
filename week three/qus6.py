class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def annual_salary(self):
        return self.salary*12
e1=employee("kira",200)
print(e1.annual_salary())

        