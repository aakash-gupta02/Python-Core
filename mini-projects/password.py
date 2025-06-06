import random
from string import ascii_letters, digits


passwordLen = int(input("EnterPassword Length: "))

if passwordLen < 6 :
    print("Number Should be greater than 6 ")
else:
    div = passwordLen//3

    let = random.choices(ascii_letters, k= div)
    let2 = random.choices(digits, k= div)
    let3 = random.choices("%#^@%!^@", k= div)

    passw = let+let2+let3

    shuf = random.shuffle(passw)

    genPassword = "".join(passw)

    print(f"Password:- {genPassword} ")