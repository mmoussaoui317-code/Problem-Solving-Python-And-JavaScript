"""OPP: seance what's mean and which languages Are interpreter and compile 
    python it's a language interpreter and Language C are a compile Structures
"""

"""
    app management of students:
        class student:
            cine: "",
            name: "",
            last_name: "",
            age: 0,

            def learning(self, cine, name, last_name, age):
                print("Hello I'm busy Hour of the Learn")
                print(self)
        

    The Class Is The shape can create it to define a new type but this type has more proprieties and methods
"""

# class Point:
#     "It Is A definition OF place Geometric"
#     x: 0
#     y: 0
#     def show(self):
#         print(self.x)
#         return self
#     pass

# # constructor by default 
# # if i'm define one new constructor the default is disappear "hidden"
# x = Point()



# p = Point()
# p.x = 0

# print(p)
# print(dir(p))
# print(p.__doc__)
# print(p.show())



# define a constructor by use the def __init__() inner the class this a pre_defined function

# Example
# the keyword this in the javascript is equal to self in python
class Student:
    "new shape of the Student has defined constructor"
    number_student = 0
    def __init__(self, cine = "", full_name = "", age = 0, *others):
        self.cine = cine
        self.full_name = full_name
        self.age = age
        self.others = others
        self.__code = self.cine * len(self.others) 

    def get__code(self):
        return self.__code
    
    def set__code(self, code = ""):
        self.__code.join(code)
        return "Success"
    
    @classmethod
    def manage_number_student(cls):
        cls.number_student += 1
    
    def __str__(self):
        return f"{self.__str__}"


first_student = Student("WE7458", "Khalid", 15, 14, 18.99, "yse can do it when ever")

print(first_student.others)
# print(dir(first_student))
# print(first_student.__doc__)

# # Manage The Privates Proprieties
# print(first_student.get__code())
# print(first_student.set__code("DWE417"))





# def multiVar(*others):
#     return others


# print(multiVar("hello how are you", 14, "can you catch this"))




# **************************************************************************************************
# ************************** IMPORTANT NOTIONS *****************************************************
# **************************************************************************************************

# must re define every operand inner the classes to use it like  * / // - + .... by usage of the pre_defined Methods Like __add__ __eq__ .....
# this is represent the current Object Compiled or interpreted