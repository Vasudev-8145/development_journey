"""
==> OBJECT ORIENTED PROGRAMMING

        --> way of programming for converting real world objects to programm

--> Class

        --> pla,design pattern,template,blueprint for creating object

--> Object

        --> realworld entity.Created using class

--> self

        --> a keyword used to call a current class 

--> constructor

        --> Initialize attributes
            Name of constructor is __init__
            Automatically called while creating object of a class

--> Inheritance

        --> child class inherits the methods and proporties of parent class

        --> Single level inheritance   : one parent class one child class
        --> Multi level inheritance    : one parent,grandparent class for child class
        --> Multiple level inheritance : multiple parents for child class

--> super

        --> a keyword used to call a parent class constructor

--> Syntax

class ClassName:

    attribute1:type
    attribute2:type
    attribute3:type

    def method_name1(self):
        method definition

    def method_name2(self):
        method definition

object_name1 = ClassName()
object_name2 = ClassName()


"""


# exp1

class Animal:

    name:str
    sound:str

    def walk(self):
        print("Animal is walking")

    def sleep(self):
        print("Animal is sleeping")

cat_instance = Animal()
dog_instance = Animal()
elephant_instance = Animal()

elephant_instance.walk()