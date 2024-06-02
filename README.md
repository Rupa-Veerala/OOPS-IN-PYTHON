# OOPS-IN-PYTHON


 **Intro**

 object oriented programming system.

 **classes & objects**

 for example we are constructing a house.

 planning is a class.

 And implementation is a object.

 **Constructors**

 it is nothing but object creation, and intialize, at the same time if we are setting propertites.

 name is always fixed   def __init__(self):

 In constructors we don't need to call functions and methods directly.

 two methods are there

 1) default   __init__

 2) parameterized

**Types of Attributes**

1) Instance attributes

   It is nothing but object, indirectly we call object attribute.

   And it is different for every object.

2) class attributes

   same for all objects of a class.

**Types of methods/(functions):**

Two methods:

1) Static method:

   it is same for all the objects.

   we can use class name for calling.

   we use @static method--> just to know the intepreter.

   in python @ means decorator.

2) Instance method:

   corresponds to a particular object.

   and it behaviour depends on the particular object.

   we use only object for calling.

**Access Modifiers**

It applies  for restrictions.

In python three types of modifiers

> public modifier.

> private modifier.

> protected modifier.

                                                            public        private          protected
Within the same class(method1)--------                       Yes           Yes                Yes

with in the derived class(inheritance)-----                  Yes            No                Yes

Within the outside class(method2)-------                     Yes            No                 No

private modifier is defined as double underscore:  __name

protected modifier is defined as single underscore:  _name
   
**Inheritance**

Inheritance allows us to define a class that inherits all the methods and properties from another class.

It has two classes.

Parent class: also called the base class and is the class being inherited.

child class: also called the derived class, and the class inherits the another class.

Types of inheritance:

-->**Single Inheritance**

ex:  X--Inherits------------>Y

-->**Multiple inheritance**

ex: X          Y
          Z

--> **Multi Inheritance**

EX: X-Grand parent-->Y--parent->Z(child)

--> **Hieraichial Inheritance**

ex: X can produce all child classes.

--> **Hybrid Inheritance**

--> It will mix 2 or more than types.

--> But not allowed the single inheritance.

--> The main purpose of inheritance is "Code Reusability"

**Polymorphism**

--> Poly means multiple.

--> morphism means forms.

--> "mul" is the common function.

**Expection Handling**

--> two types of errors compile time error, runtime error.

--> complie time error means it's a syntax error.

--> runtime error means syntax is 100% correct but after running the code then will get the error.

**Handling**

--> using try & except.

--> "Exception" can change the normal flow of the program.

--> "try" we can write the critical code.

--> "Except" if we get the exception then what can do..

--> Then we use "Finally" operation.

--> And exception is an object.

**Modules & packages**

--> Difference between files & floders.

--> Inside floders we can create files or floders.

--> Inside file only content will be there.

--> "packages" means floders that hold python files or other floders.

--> "Modules" nothing but python files.

--> "pip"--python package manager.

--> Django, flask, are the python web developement frame works for backend.

**Abstraction**

--> Hiding unnecessary details.

--> Abstract--classes ---> In python directly not support.

--> Abstarct--methods ---> we use modules then only support.

**File Handling**

--> we will do operations on files.(read, write, update)

--> two possibilites open(), close().

ex: f = open(filename, mode)  

--> mode type: t--textfile, b---binaryfile.

--> r--read, a--append, w--write, x--create.



