﻿# OOPS-IN-PYTHON


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
   
