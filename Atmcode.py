card=input("enter the card:")
if card=="credit card" or "debit card":
    print("card successfully inserted")
    language=input("enter the language:")
    if language=="English" or "Hindi":
        print("language")
        pin=int(input("enter the pin:"))
        if pin<=10000:
            print("correct")
            transaction_mode=input("enter the transaction mode:")
            if transaction_mode=="Deposit" or "Transfer" or "Withdrawal":
                print("Next")
                account_type=input("enter the type of account:")
                if account_type=="saving account" or "current account":
                    print("Next")
                    amount=int(input("enter the amount:"))
                    if amount<=15000:
                        print("Next")
                        collect_cash=input("collect the cash amount:")
                        if collect_cash=="collect your cash":
                            print("Next")
                            receipt=input("take the receipt if needed:")
                            if receipt=="yes" or "no":
                                print("Next")
                                Thank_you=input("Thank you for using Atm:")
                                if Thank_you=="visit again":
                                   print("Thank you")
                                else:
                                    print("No need")
                            else:
                                 print("No")
                        else:
                             print("invalid")
                    else:
                        print("error")
                else:
                    print("no")
            else:
                print("dont know")
        else:
            print("error")
    else:
        print("no")
else:
    print("nothing")





                                

