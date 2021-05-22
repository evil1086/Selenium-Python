class Calculator(object):

    num = 100

    def __init__(self, a, b):
        self.first = a
        self.second = b
        print('inside of the default constructor')

    def getData(self):
        print('inside of the method')

    def Summation(self):
        print(self.num + self.first + self.second)


obj = Calculator(2, 5)
obj.getData()
obj.Summation()



