secret = 5
guess = 5

if (diff := guess - secret) > 0:
    print("too high")

elif (diff := guess - secret) < 0:
    print("too small")

else:
    print("just rigth")
    
