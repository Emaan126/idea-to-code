import random
random.seed(6)
def comp_choice(list):
    return (random.choice(list))

def player_choice(list):
    player_move=input(f"Choose either, {list}")
    
    while player_move not in list:
        print("It was not valid choose again")
        player_move=input(f"Choose either, {list}")
    
    return player_move

def comparechoice(comp,player):
    if player==comp:
        print("Draw")
    elif player=="Paper":
        if comp=="Rock":
            print("Player Wins!")
            return "Player"
        else:
            print("Player Loses!")
            return "Computer"
    elif player=="Scissors":
        if comp=="Paper":
            print("Player Wins!")
            return "Player"
        else:
            print("Player Loses!")
            return "Computer"
    else:
        if comp=="Scissors":
            print("Player Wins!")
            return "Player"
        else:
            print("Player Loses!")
            return "Computer"


def updatescore (Winner, player_score, comp_score):
    if Winner=="Player":
        player_score+=1
        print("Yah")
    else:
        comp_score+=1
    return player_score, comp_score

def final_score(comp_final, player_final):
    print(f"The player has {player_final} The computer has {comp_final}")

    if comp_final==player_final:
        print("It's a Draw!")
    elif comp_final > player_final:
        print("The Computer Wins!")
    else:
        print("The Player Wins!")

def main_game ():
    options=["Rock", "Paper", "Scissors"]
    player_score=0
    comp_score=0
    number_rounds=5
    print(f"This is the one and only {options} Game!")
    print(f"How to play this game is to choose either {options}")
    print("Rock beats Scissors")
    print("Scissors beats Paper")
    print("Paper beats Rock")
    print(f"There are {number_rounds} rounds")
    print("Good Luck!")
    for i in range(number_rounds):
        comp_move=comp_choice(options)
        player_move=player_choice(options)
        Winner=comparechoice(comp_move,player_move)
        player_score,comp_score=updatescore(Winner,player_score,comp_score)
    final_score(comp_score,player_score)

main_game()

