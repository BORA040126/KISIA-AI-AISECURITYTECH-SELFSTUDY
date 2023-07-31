class first:
    def __init__(self, num1, num2):
        self.num1=num1
        self.num2=num2
    def input(self, num1):
        sum=num1+2
        return sum
    
class second(first):
    def __init__(self, num1, num2, num3):
        super().__init__(num1,num2)
        self.num3=num3

    def input(self, num1, num2, num3):
        sum_value=super().input(num1)+num2+num3
        print(sum_value)
    
c=second(1,2,3)
