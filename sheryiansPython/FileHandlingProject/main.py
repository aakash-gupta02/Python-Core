from pathlib import Path
import os

def readFolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1}: {items}")


def createFile():
    try:
        readFolder()
        name = input("Enter a File Name:-")
        p = Path(name)
        if not p.exists(): 
            with open(p,'w') as fs:
                data = input("Enter the Content:-")
                fs.write(data)
        else:
            print("File Alredy Exists")        

        print("FILE CREATED SUCCESSFULLY")

    except Exception as err:
        print(f"An Error Occured, {err}")        

def readFile():
    readFolder()

    try:
        name = input("Enter a file Name u Want to Read:- ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print(data)

            print("Readed Successfully")
    except Exception as err:
        print(f"An Error Occured, {err}")        

def updateFile():
    readFolder()

    try:
            name = input("Enter a file Name u Want to Read:- ")
            p = Path(name)
            if p.exists() and p.is_file():
                with open(p,'r') as fs:
                    data = fs.read()
                    print(data)

                print("What would U like to Update")
                print("Press 1 for Updating Name")
                print("Press 2 for Over Writing File")
                print("Press 3 for Adding New content on File")
    
                updateChoice = int(input("Enter what u want to perform:- "))        

                if updateChoice == 2:
                    with open(p,'w') as fs:
                        updateData = input("Enter Over Writing Content")
                        fs.write(updateData)

                elif updateChoice == 3:
                    with open(p,'a') as fs:
                        updateData = input("Enter Writing Content")
                        fs.write(updateData)
                
                elif updateChoice == 1:

                    name2 = input("Enter a New file Name:- ")
                    p2 = Path(name2)
                    p.rename(p2)

                else:
                    print("Enter a Number from Options")

    except Exception as err:
            print(f"An Error Occured, {err}")     

def deleteFile():
    readFolder()


    name = input("Enter a file Name to Delete:- ")
    p = Path(name)
    if p.exists() and p.is_file():
        os.remove(p)

        print("FILE DELETED SUCCESSFULLY")
    

print("Press 1 for Creating a file")
print("Press 2 for Reading a file")
print("Press 3 for Writeing a file")
print("Press 4 for Deleteing a file")

choice = int(input("Enter what u want to perform:- "))


if choice == 1:
    createFile()

elif choice == 2:
    readFile()

elif choice == 3:
    updateFile()

elif choice == 4:
    deleteFile()