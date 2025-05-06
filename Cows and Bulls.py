code = input("Enter your secret 4-digit number (do not repeat digits): ")
code_list = list(code)


guess = 0
bulls = 0
cows = 0
while(True):
    guess = input("Enter your guess for the code: ")
    guess_list = list(guess)

    bulls = 0
    cows = 0

    for i in range(len(guess_list)):
        for j in range(len(code_list)):
            if(guess_list[i] == code_list[i]):
                bulls +=1
                break
            elif(guess_list[i] == code_list[j]):
                cows +=1
            
    if(bulls == 4):
        print("You got it right!")
        break

    print("Bulls: " + str(bulls))
    print("Cows: " + str(cows))