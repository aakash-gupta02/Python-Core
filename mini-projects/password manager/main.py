master = input("Enter Master Password: ")

print("What would like to do? view or add,")

mode = input("Enter view or add: ")

def addpswd():
    passname = input("Enter Password Name: ")
    pswd = input("Enter your password: ")

    with open("allPassword.txt",'a') as fs:
        fs.write(f"Name: {passname}, Password: {pswd} \n ")


def viewpswd():
    with open("allPassword.txt",'r') as fs:
        print(fs.read())

if mode == "add":
    addpswd()

if mode == "view":
    viewpswd()
    
