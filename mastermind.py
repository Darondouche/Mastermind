#Jeu Mastermind 

refArray = ["blue", "yellow", "red", "green"]
secret_code = ["yellow", "green"]

def check_possible_colors(refArray, secret_code) :
    check = 0
    for i in refArray :
        for j in secret_code :
            if i == j : 
                check += 1
    if check == 2 :
        print("true") 
    else :
        print("false")

check_possible_colors(refArray, secret_code)

