# OOPS : object Oriented Programming System

# Class : It is a blueprint of an object.
class Student :
    subject = "Python" # Class Attribute, Variable, Property

# Object : Instance of a class, real world entity
stu1 = Student() # Object Creation
stu2 = Student()
print(stu1.subject) # Accessing Class Attribute using Object
print(stu2.subject)
print(Student.subject) # Accessing Class Attribute using Class Name
print(id(stu1)) # Unique identity of Object
print(id(stu2))
print(type(stu1)) # Type of Object
print(type(stu2))
print(isinstance(stu1, Student)) # Checking the type of Object
print(isinstance(stu2, Student))
print(stu1 == stu2) # Comparing two Objects
print(stu1 is stu2)
