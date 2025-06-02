a = 1

match a:
    case 1:
        print("u selected 1")
    case 2:
        print("u slected 2")
    case 3:
        print("u selected 3")    
    case _:
        print("out of context")     


lucky_number = int(input("Enter your lucky number : "))

match lucky_number:
    case 1:
        print("🎉 You chose 1 – That's super lucky!")
    case 2:
        print("✨ Number 2 – A sign of balance and harmony!")
    case 3:
        print("🔥 Number 3 – Power and creativity!")
    case 4:
        print("💧 Number 4 – Calm and wise choice!")
    case 5:
        print("🌟 Number 5 – You shine bright today!")
    case _:
        print("😅 Not a lucky number today. Try again with 1-5.")


