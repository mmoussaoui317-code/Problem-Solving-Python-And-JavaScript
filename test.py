import random




secret = random.randrange(1,11)


gusNb = int(input("gus the secret number :  "))

if gusNb != secret :
    gusNb = int(input("second try :  "))

    if secret == gusNb :
        print("yes You got it")
    elif secret < gusNb :
        print("you're very far to it")
    else : 
        print("you're very near to it5")
else :
    print("bravo you are got it")
