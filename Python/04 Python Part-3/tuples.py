# tuples = immutable sequence of values : maybe of diff. types
tup1 = (23,35,6,5,77,5,5,54,33)
# tup1[3] = 45 => error as tuples are immutable 
print(type(tup1))
print(tup1)

tup = (1) # int type
print(type(tup))

tup = ("rohit") # string type
print(type(tup))

tup = (1,) # tuple type with single element
print(type(tup))

print(tup1.index(5))  # returns index of first occurrence of value 77
print(tup1.count(5))   # returns count of occurrences of value 5

# can also perform slicing on tuples
print(tup1[2:5])