nums = [1,2,3,4,5]

for num in nums: 
    print(num)

# searching for 3 element & printing it's index i.e. 2
# linear_search
x = 4 
idx = 0
for val in nums :
    if(val == x) :
        print(f"{x} found at idx = {idx}")
        break
    idx += 1

