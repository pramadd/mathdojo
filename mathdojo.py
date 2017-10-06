class Mathdojo(object):
    def __init__(self):
        self.result=0
    
    def add(self, *num):
        for i in num:
            if isinstance(i,int): 
                self.result=self.result+i
                print "adding numbers " ,self.result
            else:
                for number in i:
                    self.result=self.result + number
                    print "adding number", self.result
        return self

    def subtract(self, *num):
        for i in num:
            if isinstance(i,int):
                self.result=self.result-i
                print "subtracting number", self.result
            else:
                for number in i:
                    self.result=self.result - number
                    print "subtracting number",self.result

        return self
#PART I result
md=Mathdojo()               
md.add(2).add(2,5).subtract(3,2).result
print ''


#PART II result
md=Mathdojo()         
md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result         


       