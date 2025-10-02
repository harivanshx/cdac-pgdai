username =  input("Enter a username ::::")
if len(username)>12:
    print("username cant be more than 12")
elif username.find(" ") != -1:
    print("Username cant have spaces")
elif username.isalpha() == False:
    print("bhai number nahi please")
else:
    print("User name is good to go ") 