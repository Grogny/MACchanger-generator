from randmac import RandMac

while True:
    nb = input("[+] How many address? (max : 9) : ")
    if not nb.isnumeric():
        print("Please enter a number")
    elif int(nb) > 9:
        print("Max : 9, please enter a valid ammount of address")
    else:
        for i in range(0, int(nb)):
            print(f"[{i+1}]", RandMac("00:00:00:00:00:00"))
        break
