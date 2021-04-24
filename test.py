name = input("What is your name? \n")
main_users = ["John", "Hilary", "Jane"]
main_password = ["john", "hilary", "jane"]

if(name in main_users):
    password = input("Your password? \n")
    userId = main_users.index(name)
    
    import datetime
    now = datetime.datetime.now()
    print ("Current date and time : ")
    print (now.strftime("%Y-%m-%d %H:%M:%S"))
    
    if(password == main_password [userId]):
        
        print("Welcome %name")
        print("Available options:")
        print("1. Withdraw")
        print("2. Cash Deposit")
        print("3. Complaints")
    
        selected_option = int(input("Please select an option: "))
        
        if(selected_option == 1):
            input("How much would you like to withdraw? ")
            print("Take your cash.")
           
        elif(selected_option == 2):
            input("How much would you like to deposit? ")
            print("Current_balance = #12500")
            
        elif(selected_option == 3):
            input("What issue will you like to report? ")
            print("Thank you for contacting us.")
                
            
        else:
            print("Invalid option selected, please try again!")
        
        
    else:
        print("Password Incorrect,please try again!")
        
    
else:
    print("Name not found, please try again!")









    
