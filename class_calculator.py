class calculator:
    def __init__(self):
        self.a=0
    def mul(self, *args):
        self.init=1
        for i in args:
            self.init*=i
        return self.init
    def sum(self,*args):
        self.init=0
        for i in args:
            self.init+=i
        return self.init

cal=calculator()
print(cal.mul(1,2,3,4))
print(cal.sum(1,2,3,4,5))