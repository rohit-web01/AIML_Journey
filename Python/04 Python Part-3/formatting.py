a = 5
b = 10
sum = a + b

print("Sum is {}".format(sum))           # format function : placeholder & placeholder values
print("Sum of {} & {} is {}".format(a, b, sum))    #multiple formating
 #index based formating 
print("Sum of {0} & {1} is {2}".format(a, b, sum))
# value based formating
print("sum of {a} & {b} is {sum}".format(a=a, b=b, sum=sum))


##### F_strings #####
print(f"Sum is {sum}")           # f_string : placeholder & placeholder values
print(f"sum of {a} & {b} is {sum} through f_string")
print(f"avg of {a} & {b} is {sum/2}")