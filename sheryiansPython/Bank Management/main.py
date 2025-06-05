import json
import random
from pathlib import Path
import string

class Bank:
    database = 'data.json'
    data = []

    try:

        if Path(database).exists():
            with open(database, 'r') as fs:
                # data = [json.loads(fs.read())]
                data = json.loads(fs.read())

        else:
            print("No file exists")

    except Exception as err:
        print(err)



    @staticmethod
    def updateData():
        with open(Bank.database,'w') as fs:
            fs.write(json.dumps(Bank.data))


    @classmethod
    def generateID(cls):
        alpha = random.choices(string.ascii_letters, k=4)
        num = random.choices(string.digits,k = 2)
        spSym = random.choices("!@#@%", k=2)
        id = alpha + num + spSym
        random.shuffle(id)
        return "".join(id)


    def createAccount(self):
        info = {
            "name": input("Tell your name :- "),
            "age" : int(input("tell your age :- ")),
            "email": input("tell your email :- "),
            "pin": int(input("tell your 4 number pin :- ")),
            "accountNo." : Bank.generateID(),
            "balance" : 0
        }
        if info['age'] < 18  or len(str(info['pin'])) != 4:
            print("sorry you cannot create your account")
        else:
            print("account has been created successfully")
            for i in info:
                print(f"{i} : {info[i]}")
            
            print("please note down your account number")

            Bank.data.append(info)
            Bank.updateData()


    def depositMoney(self):

        id = int(input("Enter Your ID:- "))
        

        userData = [i for i in Bank.data if i['accountNo.'] == id ]

        if userData:
            pin = int(input("Enter Your PIn:- "))

            if pin != userData[0]['pin']:
                print("Enter Corrrect Pin")
            else:
                money = int(input("Enter the Amount:- "))    
                if money < 0 or money > 100000:
                    print("Amount should be less than 100,000")
                else:
                    userData[0]['balance'] += money    
                    Bank.updateData()
                    print("Money Deposited Successfully")

                    print('********************************')
                    print(f"Final Balnce is: {userData[0]['balance']}")

    def withdrawMoney(self):

        id = int(input("Enter your Account Number"))

        userData = [i for i in Bank.data if i['accountNo.'] == id ]

        if userData:
            pin = int(input("Enter your PIN"))

            if pin != userData[0]['pin']:
                print("Enter Corrrect PIN")

            else:
                print(f"Account Balance is: {userData[0]['balance']}")
                amount = int(input("Enter the Withdrawing Amount: "))

                if amount > userData[0]['balance']:
                    print("!!Insufficient Balance")
                else:
                    userData[0]['balance'] -= amount
                    print("Money WithDrawed Successfully")    
                    print("******************************")
                    print(f"Final Balnce is: {userData[0]['balance']}")
                    print("Thank you")

    def showDetails(self):

        id = int(input("Enter your Account Number: "))

        userData = [i for i in Bank.data if i['accountNo.'] == id ]

        if userData:
            pin = int(input("Enter your PIN: "))

            if pin != userData[0]['pin']:
                print("Enter Corrrect PIN")
                Bank.showDetails()

            else:
                for i in userData[0]:

                    if i == 'pin':
                        continue
                    print(f"{i}: {userData[0][i]} ")


    def updatedetails(self):
            accnumber = input("please tell your account number ")
            pin = int(input("please tell your pin aswell "))

            userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

            if userdata == False:
                print("no such user found ")
            
            else:
                print("you cannot change the age, account number, balance")

                print("Fill the details for change or leave it empty if no change")

                newdata = {
                    "name": input("please tell new name or press enter : "),
                    "email":input("please tell your new Email or press enter to skip :"),
                    "pin": input("enter new Pin or press enter to skip: ")
                }

                if newdata["name"] == "":
                    newdata["name"] = userdata[0]['name']
                if newdata["email"] == "":
                    newdata["email"] = userdata[0]['email']
                if newdata["pin"] == "":
                    newdata["pin"] = userdata[0]['pin']
                
                newdata['age'] = userdata[0]['age']

                newdata['accountNo.'] = userdata[0]['accountNo.']
                newdata['balance'] = userdata[0]['balance']
                
                if type(newdata['pin']) == str:
                    newdata['pin'] = int(newdata['pin'])
                

                for i in newdata:
                    if newdata[i] == userdata[0][i]:
                        continue
                    else:
                        userdata[0][i] = newdata[i]

                Bank.updateData()
                print("details updated successfully")


    def deleteAcc(self):

        id = int(input("Enter your Account Number"))

        userData = [i for i in Bank.data if i['accountNo.'] == id ]

        if userData:
            pin = int(input("Enter your PIN"))

            if pin != userData[0]['pin']:
                print("Enter Corrrect PIN")

            else:
                print("Are You Sure that, You want to Delete this Account")
                sure = input("Type Yes or No")

                if sure == "Yes":

                    index = Bank.data.index(userData[0])
                    Bank.data.pop(index)
                    Bank.updateData()
                    print("Account Deleted Successfuly")

                elif sure == "No":
                    print("Account Deletion Cancelled")
                else:
                    print('Type Exact "Yes" or "No"\n or leave it as it is! ')    

user = Bank()
print("press 1 for creating an account")
print("press 2 for Deposititing the money in the bank ")
print("press 3 for withdrawing the money ")
print("press 4 for details ")
print("press 5 for updating the details")
print("press 6 for deleting your account")


choose = int(input("Enter what u want to erform:- "))

if choose == 1:
    user.createAccount()

elif choose == 2:
    user.depositMoney()

elif choose == 3:
    user.withdrawMoney()

elif choose == 4:
    user.showDetails()

elif choose == 5:
    user.updatedetails()

elif choose == 6:
    user.deleteAcc()