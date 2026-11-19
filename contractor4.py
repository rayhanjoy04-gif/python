class student():
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def get_avg(self):
        sum=0
        for val in self.mark:
            sum+=val
        print("Hi",self.name,"your acg score is:",sum/3)
s1=student("tony stack",[99,98,97])
s1.get_avg()
s1.name="Rayhan"
s1.get_avg()                
