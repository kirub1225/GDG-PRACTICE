class bankaccount:
    def __init__(self):
        self.__balance=0
    def deposit(self,amount):
        self.__balance+= amount
    def withdraw(self,amount):
        if(amount>self.__balance):
            print("insufficient amount")
            return -1
        self.__balance-= amount
    def get_balance(self):
        return self.__balance 
b1=bankaccount()
b1.withdraw(1)



        