import random
print("WELCOME TO guessing number GAME ")
response= input("Do You Want To Play The Game: ")
if response.lower() !="yes":
    quit()
range= input("enter a number: ")
if range.isdigit():
    range=int(range)
    if range<0:
        print("please enter a number larger than 0 ")
        quit()
else:
    print("please enter a number ")
    quit()
random_number= random.randint(0,range)
chances= 0
while True:
    chances+=1
    user_input= input("guess a number: ")
    if str(user_input).isdigit():
        user_input=int(user_input)
    else:
        print("please enter a number larger than 0 ")
        quit()
    
    if user_input== random_number:
        print("your guuess is correct ")
        break
    elif user_input<random_number:
        print("your guess is   low ")
    else:
        print("your guess is  high ")  
print("you got it in ", chances,"guesses")
