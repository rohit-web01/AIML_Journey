word = "python"

print(len(word))        # 6
sentence  = "I love " + word
print(sentence)

# index values starting from 0
print(word[3])

# word[2] = 'm'  : wrong: string in python are inmutable

# traversing
for ch in word :
    print(ch)