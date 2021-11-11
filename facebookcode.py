name=input("enter the name:")
if name==name:
    print(name)
    Dob=input("enter the dob:")
    if Dob==(Dob):
        print(Dob)
        mob_no=int(input("enter the mob_no:"))
        if mob_no>=1000000000 and mob_no<=10000000000:
            print(mob_no)
            email=input("enter the email:")
            if email and "@gmail.com" in email:
                print(email)
                gender=input("enter the gender:")
                if gender=="female" or "male" or "custom":
                    print(gender)
                    password=input("enter the password:")
                    if password >="letters" and "symbols" and "number":
                       print(password)
                       sign_up=input("please sign_up:")
                       if sign_up=="yes":
                           print(sign_up)
                           to_finish_your_sign_up=input("confirm your mob_no and email:")
                           if to_finish_your_sign_up=="mob_no" or "email":
                               print(sign_up)
                           else:
                               print("go back and check the details again")
                       else:
                           print("No")
                    else:
                        print("Wrong password")
                else:
                    print("Wrong gender")
            else:
                print("wrong email")
        else:
            print("mob_no not matched")
    else:
        print("wrong Dob")
else:
    print("please enter the name correctly")                                              


                           
