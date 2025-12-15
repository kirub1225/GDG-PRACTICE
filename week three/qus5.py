class student:
    def setter(self,grade):
        self.__grade=grade
    def getter(self):
        return self.__grade
c1=student()
c1.setter("a")
print(c1.getter())
