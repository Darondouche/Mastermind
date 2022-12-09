#Jeu Mastermind 

refArray = ["blue", "yellow", "red", "green"]
secret_code = ["yellow", "gray"]
choicePlayer = []

def check_possible_colors(refArray, secret_code) :
    check = 0
    for i in refArray :
        for j in secret_code :
            if i == j : 
                check += 1
    if check == 2 :
        return 2 == check 
    else :
        return 0 == check

def check_combinaison(secret_code, choicePlayer):
   return secret_code == choicePlayer

def initiate_game():
    choicePlayer = input("Guess two colors : ").split(" ")
    chances = 1
    if check_possible_colors(refArray, secret_code) == True :
            while ((check_combinaison(secret_code, choicePlayer) == False) and (chances < 12)) :
                choicePlayer = input("Guess again : ").split(" ") 
                chances += 1
            if chances == 12: 
                print("You loose !")
                return
            else :
                print("You won !")
                return
    else :
        print("The secret code is invalide.")
        return

initiate_game() 


