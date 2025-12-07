info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English"),
]

course = set()
stu_in_eng = []
dict = {}

for name, subject in info:
    if(dict.get(name) == None) :
        # dict["name"] = (subject)
        dict.update({name : set()})
        dict[name].add(subject)
    else:
        dict[name].add(subject) 

    course.add(subject)
    if(subject == "English") :
        stu_in_eng.append(name)


print(course)
print(stu_in_eng)
print(dict)