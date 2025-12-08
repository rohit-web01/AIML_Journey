name = input("Enter Your Name : ")
cgpa = float(input("Enter Your CGPA : "))

class Student : 
    # class attributes
    college = "School Of Information Technology"
    Rating = 5
    def __init__ (self) :
        print("NEW REGISTRATION STARTED : ")

    # Only one constructor || init method allowed in python :: it will execute the one written in last.
    def __init__(self, name, cgpa) :     # parameterised constructor
        print(f"{name}, is registered successfully.")
        # instance attributes
        self.name = name
        self.cgpa = cgpa
        self.Rating = 1

    def get_cgpa(self) :
        return self.cgpa

stu1 = Student(name, cgpa)
print(Student.college)  # will be correct 
print(f"College Rating : {Student.Rating}")
print(f"Student Name : {stu1.name}")
print(f"CGPA : {stu1.get_cgpa()}")
print(f"Student Rating : {stu1.Rating}")