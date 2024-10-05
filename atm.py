import pwinput
from openpyxl import load_workbook
excel_file="atm_database.xlsx"
class user:
    def __init__(self, user_id, pin, balance):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance

def create_user():
    members = [
        user(1111,1234, 10000),
        user(2222,5678, 8500),
        user(3333, 2468, 9500)
    ]
    return members
def usage(user_id,pin,members):
    u=int(user_id)
    v=int(pin)
    if(u==1111):
        if(v==1234):
            transactions=[]
            while True:
                x=members[0]
                print("Welcome,what service would you like to use")
                print("Press 1 for Withdraw")
                print("Press 2 for Deposit")
                print("Press 3 for Transfer")
                print("Press 4 for transaction history")
                print("Press 5 to quit")
                print("Press 6 to check balance")
                ch=int(input("Enter choice: "))
                if(ch==1):
                    a=(input("Enter amount to withdraw: "))
                    if(a.isdigit()):
                        if(int(a)<=x.balance):
                            x.balance=int(x.balance)-int(a)
                            transactions.append((f"${a} has been withdrawn from your account."))
                            print("Withdrawl complete,Remaining balance")
                            print(x.balance)
                            print("\n")
                        else:
                            print("Insufficient balance")
                            print("\n")
                    else:
                        print("Invalid Input")
                        
                elif(ch==2):
                    a=(input("Enter amount to deposit: "))
                    if(a.isdigit()):
                        x.balance=int(x.balance)+int(a)
                        transactions.append((f"${a} has been deposited into your account."))
                        print("Deposit complete,Remaining balance")
                        print(x.balance)
                        print("\n")
                    else:
                        print("Invalid Input")
                elif(ch==3):
                    a=(input("Enter amount to transfer: "))
                    b=(input("Enter the user_id to transfer"))
                    print(b)
                    if(a.isdigit() and b.isdigit()  ):
                        if(int(b)==2222):
                            y=members[1]
                            if(int(a)<=x.balance):
                                x.balance=int(x.balance)-int(a)
                                y.balance=int(y.balance)+int(a)
                                transactions.append((f"${a} has been transfered from your account to {b}."))
                                print(x.balance)
                                print(y.balance)
            
                            else:
                                print("Insufficient balance")
                                print("\n")
                        elif(b==3333):
                            y=members[2]
                            if(a<=x.balance):
                                x.balance=int(x.balance)-int(a)
                                y.balance=int(y.balance)+int(a)
                                transactions.append((f"${a} has been transfered from your account to{b}."))
                                print(x.balance)
                                print(y.balance)
                            else:
                                print("qidbc")
                                print("Insufficient balance")
                                print("\n")
                    else:
                        print("Invalid Input check for positive values or correct user id")
                elif(ch==4):
                    for transaction in transactions:
                        print(transaction)
                    print("\n")
                elif(ch==5):
                    print("Thank You for using the ATM. Have a Nice Day!!!")
                    break
                elif(ch==6):
                    print(x.balance)
        else:
            print("Wrong Pin,process terminated")
    elif(u==2222):
        if(v==5678):
            transactions=[]
            while True:
                x=members[1]
                print("Welcome,what service would you like to use")
                print("Press 1 for Withdraw")
                print("Press 2 for Deposit")
                print("Press 3 for Transfer")
                print("Press 4 for transaction history")
                print("Press 5 to quit")
                print("Press 6 to check balance")
                ch=int(input("Enter choice: "))
                if(ch==1):
                    a=(input("Enter amount to withdraw: "))
                    if(a.isdigit()):
                        if(int(a)<=x.balance):
                            x.balance=int(x.balance)-int(a)
                            transactions.append((f"${a} has been withdrawn from your account."))
                            print("Withdrawl complete,Remaining balance")
                            print(x.balance)
                            print("\n")
                        else:
                            print("Insufficient balance")
                            print("\n")
                    else:
                        print("Invalid Input")
                        
                elif(ch==2):
                    a=(input("Enter amount to deposit: "))
                    if(a.isdigit()):
                        x.balance=int(x.balance)+int(a)
                        transactions.append((f"${a} has been deposited into your account."))
                        print("Deposit complete,Remaining balance")
                        print(x.balance)
                        print("\n")
                    else:
                        print("Invalid Input")
                elif(ch==3):
                    a=(input("Enter amount to transfer: "))
                    b=(input("Enter the user_id to transfer"))
                    if(a.isdigit() and b.isdigit() ):
                        if(b==1111):
                            y=members[0]
                            if(a<=x.balance):
                                x.balance=int(x.balance)-int(a)
                                y.balance=int(y.balance)+int(a)
                                transactions.append((f"${a} has been transfered from your account."))
                                print(x.balance)
                                print(y.balance)
            
                            else:
                                print("Insufficient balance")
                                print("\n")
                        elif(b==3333):
                            y=members[2]
                            if(a<=x.balance):
                                x.balance=int(x.balance)-int(a)
                                y.balance=int(y.balance)+int(a)
                                transactions.append((f"${a} has been transfered from your account."))
                                print(x.balance)
                                print(y.balance)
                            else:
                                print("Insufficient balance")
                                print("\n")
                        else:
                            print("check for positive values or correct user id")
                    else:
                        print("Invalid Input ")
                elif(ch==4):
                    for transaction in transactions:
                        print(transaction)
                    print("\n")
                elif(ch==5):
                    print("Thank You for using the ATM. Have a Nice Day!!!")
                    break
                elif(ch==6):
                    print(x.balance)
        else:
            print("Wrong Pin,process terminated")
    elif(u==3333):
        if(v==2468):
            transactions=[]
            while True:
                x=members[2]
                print("Welcome,what service would you like to use")
                print("Press 1 for Withdraw")
                print("Press 2 for Deposit")
                print("Press 3 for Transfer")
                print("Press 4 for transaction history")
                print("Press 5 to quit")
                print("Press 6 to check balance")
                ch=int(input("Enter choice: "))
                if(ch==1):
                    a=(input("Enter amount to withdraw: "))
                    if(a.isdigit()):
                        if(int(a)<=x.balance):
                            x.balance=int(x.balance)-int(a)
                            transactions.append((f"${a} has been withdrawn from your account."))
                            print("Withdrawl complete,Remaining balance")
                            print(x.balance)
                            print("\n")
                        else:
                            print("Insufficient balance")
                            print("\n")
                    else:
                        print("Invalid Input")
                        
                elif(ch==2):
                    a=(input("Enter amount to deposit: "))
                    if(a.isdigit()):
                        x.balance=int(x.balance)+int(a)
                        transactions.append((f"${a} has been deposited into your account."))
                        print("Deposit complete,Remaining balance")
                        print(x.balance)
                        print("\n")
                    else:
                        print("Invalid Input")
                elif(ch==3):
                    a=(input("Enter amount to transfer: "))
                    b=(input("Enter the user_id to transfer"))
                    if((a.isdigit() and b.isdigit() )and (b==2222 or b==1111)):
                        if(b==1111):
                            y=members[0]
                            if(a<=x.balance):
                                x.balance=int(x.balance)-int(a)
                                y.balance=int(y.balance)+int(a)
                                transactions.append((f"${a} has been transfered from your account."))
                                print(x.balance)
                                print(y.balance)
            
                            else:
                                print("Insufficient balance")
                                print("\n")
                        elif(b==3333):
                            y=members[2]
                            if(a<=x.balance):
                                x.balance=int(x.balance)-int(a)
                                y.balance=int(y.balance)+int(a)
                                transactions.append((f"${a} has been transfered from your account."))
                                print(x.balance)
                                print(y.balance)
                            else:
                                print("Insufficient balance")
                                print("\n")
                    else:
                        print("Invalid Input check for positive values or correct user id")
                elif(ch==4):
                    for transaction in transactions:
                        print(transaction)
                    print("\n")
                elif(ch==5):
                    print("Thank You for using the ATM. Have a Nice Day!!!")
                    break
                elif(ch==6):
                    print(x.balance)
        else:
            print("Wrong Pin,process terminated")
        


def main():
    print("Welcome to Python ATM\n")
    print("Successfully inserted Card\n")
    user_id = input("Please Enter your User id : ")
    pin = pwinput.pwinput(prompt='Enter your pin:  ', mask='*')
    members=create_user()
    usage(user_id,pin,members)

if __name__ == "__main__":
    main()