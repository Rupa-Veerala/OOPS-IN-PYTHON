class Person:
    def __init__(self,name,age):
        self.__name = name
        self.age = age
    def getValue(self):
        print(self.__name)
p=Person("Rupa",10)
p.getValue()
print(p.__name)

"""here print rupa because rupa is with in the same class in private modifiers having full restrictions so it will print with in the same class only and outside and derived class will not print """
