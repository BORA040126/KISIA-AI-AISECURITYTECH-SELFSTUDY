class sum:
    def __init__(self):
        self.result=0

    def add(self,num):
        self.result+=num #self.result=self.result+num
        return self.result
    
cal1=sum()
cal2=sum()

print(cal1.add(2))
print(cal1.result)
print(cal1.add(3))
print(cal2.add(2))
print(cal2.add(6))

