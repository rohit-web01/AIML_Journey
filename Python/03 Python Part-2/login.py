username = input("Enter your username: ")
password = int(input("Enter your password: "))

if (username == "admin" and password == 123):
    print("LOGIN Successfully.")
elif username != "admin" :
    print("username is incorrect.")
else : 
    print("Password is wrong.")