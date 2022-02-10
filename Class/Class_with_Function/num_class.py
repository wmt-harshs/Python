
class Number:

    def __init__(self,number):
        
        self.number = number

    def Check_number(self):
        
        if len(self.number) == 10:
            print("Valid Number") 
        else:
            print("Invalid Number")

