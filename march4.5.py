#Main program for OOPS concept for data creation,passing data and get function:

class student:
    
    def __init__(self,name,m1,m2,m3):
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3
    
    def get_total(self):
        print(f"name: {self.name}\ntotal: {self.m1+self.m2+self.m3}")
    def get_avg(self):
        print(f"average : {(self.m1+self.m2+self.m3)/3}")

s1=student("AADITYA",100,95,85)

s1.get_total()
s1.get_avg()

