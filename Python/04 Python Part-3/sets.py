# Sets : collection of unique elements & immutable (tuple, string)

s = {1,2,2,5,5,5,7,7}

s.add(9)  # Adding new element
s.remove(2)  # removing element
s.pop()  # removes and returns an arbitrary element
# s.clear()  # removes all elements
s.union({10,11,12})  # union of two sets
s.intersection({5,7,9,11})  # common elements in both sets
s.difference({5,7})  # elements in s but not in the other set
print(s)
empty_set = set()
print(type(empty_set))

d1 = {}      # empty dictionary
l1 = []      # list
t2 = ()      # tuple

print(type(d1))
print(type(l1))
print(type(t2))

print(len(s))
print(len(d1))
print(len(l1))
print(len(t2))