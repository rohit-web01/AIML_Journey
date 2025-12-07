# dictionary => key:value pairs (unordered, mutable)
dict = {
    "name": "Rohit",
    "age": 21,    
    "city": "Ratlam"
}

print(dict)
print(dict["name"])  # accessing value using key  || don't use 
print(dict.get("names"))  # will return none || preferalable
dict["age"] = 22  # modifying value
print(dict)
dict["profession"] = "Student"  # adding new key:value pair
print(dict)
del dict["city"]  # deleting key:value pair
print(dict)
print(dict.keys())  # getting all keys
print(dict.values())  # getting all values
print(dict.items())  # getting all key:value pairs

dict.update({
    "Country" : "India"
})
# looping through dictionary

for key, value in dict.items():
    print(f"{key}: {value}")
# checking if key exists
if "name" in dict:
    print("Name is present in the dictionary")
else:
    print("Name is not present in the dictionary")      

