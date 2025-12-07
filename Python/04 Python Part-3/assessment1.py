# 1 Palindrome check
word = input("Enter your string : ")
print(word == word[::-1])

# 2 compute average
listAvg = [1,2,7]
sum = 0
for val in listAvg :
    sum += val
avg = sum / len(listAvg)
print("Average is :", avg)

# 3 merge list and sort them
list1 = []
list2 = []

n1 = int(input("Enter Number of Elem You Want in List1 : "))
for i in range(n1) :
    ele = int(input(f"Enter Your {i+1} Element : "))
    list1.append(ele)

n2 = int(input("Enter Number Of Elements You Want in List2 : "))
for i in range(n2) :
    ele = int(input(f"Enter Your {i+1} Element : "))
    list2.append(ele)

merged_list = list1 + list2
merged_list.sort()
print(merged_list)

# Tuple of even & odd 
tup = (3,4,5,2,6,8,4)
even = []
odd = []
for val in tup :
    if(val % 2 == 0) :
        even.append(val)
    else :
        odd.append(val)
print(tup)
tup_even = tuple(even)
tup_odd = tuple(odd)
print(tup_odd)
print(tup_even)

# unique characters in string
str = "hellohello"
unique_chars = set(str)
print("Unique Characters are : ", unique_chars)
print("Number of Unique Characters are : ", len(unique_chars))

# repeated elements in list
list_rep = [1,2,3,4,5,1,2,3,6,7,8,4]
unique = set(list_rep)
repeated = []               
for val in unique :
    if(list_rep.count(val) > 1) :
        repeated.append(val)
print("Repeated Elements are : ", repeated)