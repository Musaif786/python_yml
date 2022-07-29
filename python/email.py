#from curses.ascii import isalpha


email = input("Enter mail id: \n")
if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            print("your mail is correct")
        else:
            print("wrong email") 
    else:
        print("wrong email 2")
else:
    print("you mail")