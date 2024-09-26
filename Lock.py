allKey = {143: "akksee", 674: "phonelaundering", 718: "n0tb1@nkets3et1l3"}

def lockCheck():
    whichClient = int(input("Input your id to begin: "))
    if whichClient in allKey:
        print(f"Welcome customer {whichClient}")
    else:
        print("Invalid id")
        print("Please go to one of the desks to get an account")

    passCode = input("Please enter your password: ")
    if passCode == allKey[whichClient]:
        print("Welcom to the bank of wiz")
    else:
        while True:
            print("ALARM ALARM ALARM ALARM ALARM ALARM ALARM ALARM ALARM ALARM ALARM ALARM ALARM ALARM ALARM ALARM ALARM ALARM ALARM")


