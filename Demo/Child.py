from Demo.Parent import Calculator


class Child(Calculator):

    num1 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 100)

    def num_summation(self):
        print(self.num1 + self.first + self.second)


obj1 = Child()
obj1.num_summation()

