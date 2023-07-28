class student:
    def __init__(self,name,gradYear):   
        self.name = name
        self.gradYear = gradYear
    
    def myfunc(self):
        print("Hello my name is " + self.name)
            
s1 = student("eli"," 2020")                     
s2 = student("jay"," 2021")
s3 = student("april"," 2022")
s4 = student("david"," 2023")
s5 = student("rod"," 2024")

print("Name of student is " + s2.name + s2.gradYear)
print("Name of student is " + s3.name + s3.gradYear)
print("Name of student is " + s4.name + s4.gradYear)
print("Name of student is " + s5.name + s5.gradYear)

arr = [s1,s2,s3,s4,s5]


        