import random
def player_input():
    player_choice=input ("Key in a 4 digit number")
    player_list=[]
    idx=0
    for i in player_choice:
        player_list.append(int(i))
        idx+=1
        if (idx>=4):
            break


    while len(player_list)<4:
    
            player_list.append (0)
    return(player_list)

def game_rules():
    print("The rules of Number Worlde are...")
    print("Try to guess the secret 4 digit number in 10 tries!")
    print("If one of the numbers in your digit is the same number in the secret number and the same position there will be a green circle")
    print("If one of the numbers is the correct number but in the wrong place there will be a orange circle")
    print("And if one of the numbers is not in the secret number then you will se a red circle")
    print("Good Luck!")

def hidden_key():
    number_list=[]
    for i in range(4):
        number_list.append(random.randint(0,9))
    return (number_list)

def display_hint(secret_key,player_guess):
    index=0
    game_list=[]
    for i in player_guess:
        if i not in secret_key:
            game_list.append("🔴")
        else:
            if secret_key[index]==i:
                game_list.append("🟢")
            else:
                game_list.append("🟠")
        index+=1
    print(game_list)

def main_game():
    secret_key=hidden_key()
    #secret_key=[1,2,3,4]
    #print(secret_key)
    tries=10
    game_rules()
    for i in range(tries):
        player_choice=player_input()
        print(player_choice)
        display_hint(secret_key,player_choice)
        tries-=1
        print(f"Number of tries left is {tries}")
        if (secret_key==player_choice):
            print("Well Done! You did it!")
            print("""/)  /)  ~ ┏━━━━━━━━┓
( •-• )  ~ ♡ You are amazing ♡
/づづ ~ ┗━━━━━━━━┛""")
            break
    print(f"You loose! The secret number was {secret_key}")
    print("""▄██████████████▄▐█▄▄▄▄█▌
██████▌▄▌▄▐▐▌███▌▀▀██▀▀
████▄█▌▄▌▄▐▐▌▀███▄▄█▌
▄▄▄▄▄██████████████▀""")
        
main_game()
