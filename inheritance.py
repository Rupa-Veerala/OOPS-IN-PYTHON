class Person:
    x = 20
    def eat(self):
        print("I am eating")
class Student(Person):
    rno = 25
    def write(self):
        print("I am writing")
s1 = Student()
s1.write()