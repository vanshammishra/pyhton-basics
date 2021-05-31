# here we are going to implement the concept the concept of inheritance
# in this we would import the parent class from other file to this file and it would be known as the child.
from oops1 import backchodi


class childinher(backchodi):
    num2 = 200

    def __init__(self):
        backchodi.__init__(self, 5, 7)

    def getithere(self):
        return childinher.num2 + self.summation()


obj1 = childinher()
print(obj1.getithere())
