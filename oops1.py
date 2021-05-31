# self keywords is necessary for calling the variable names into method
# new create is not required when you create a new objecttak


class backchodi:
    number = 100

    def getnumber(self):
        print("thhis is just for the experiment purpose of the oops")

    def __init__(self, a, b):
        print("constructor is called automatically when object is created")
        self.firstnumber= a
        self.secondnumber= b

    def summation(self):
          return self.firstnumber + self.secondnumber + backchodi.number
    # to call the class variable we have to call that by name of that class.variable that we wanna use


obj = backchodi(4, 6)
print(obj.summation())

obj2 = backchodi(4, 7)
print(obj2.summation())
