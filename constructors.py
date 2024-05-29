#In construcors directly we don't need to call functions & methods

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def getValue(self):
        print("The name of the person is ",self.name," and the age is ",self.age,".",sep="")
name=input()
age=int(input())
p= Person(name,age)
p.getValue()