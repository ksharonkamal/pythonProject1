class rectangle:
    def __init__(self,length,bredth):
        self.length=length
        self.bredth=bredth
    def cal_area(self):
        return self.length*self.bredth

r1=rectangle(10,20)
area=r1.cal_area()
print(area,"sq units")