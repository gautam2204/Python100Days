print('''  ,d                                                                       
  88                                                                       
MM88MMM 8b,dPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88       88 8b,dPPYba,  
  88    88P'   "Y8 a8P_____88 ""     `Y8 I8[    "" 88       88 88P'   "Y8  
  88    88         8PP""""""" ,adPPPPP88  `"Y8ba,  88       88 88          
  88,   88         "8b,   ,aa 88,    ,88 aa    ]8I "8a,   ,a88 88          
  "Y888 88          `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP'Y8 88          
                                                                           
                                                                           
                                                      
                                                      
                                                      
                                                      
 ,adPPYba, 88,dPYba,,adPYba,  ,adPPYYba, 8b,dPPYba,   
a8P_____88 88P'   "88"    "8a ""     `Y8 88P'    "8a  
8PP""""""" 88      88      88 ,adPPPPP88 88       d8  
"8b,   ,aa 88      88      88 88,    ,88 88b,   ,a8"  
 `"Ybbd8"' 88      88      88 `"8bbdP"Y8 88`YbbdP"'   
                                         88           
                                         88           
 ''')
''''
You're at a crossroad. Where do you want to go? Type "left" or "right"'
'You've come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.'
"You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?"
"It's a room full of fire. Game Over."
"You found the treasure! You Win!"
"You enter a room of beasts. Game Over."
"You chose a door that doesn't exist. Game Over."
"You get attacked by an angry trout. Game Over."
"You fell into a hole. Game Over."
'''
player_name = input("Welcome to the 'TREASURE GAME'.\nEnter your name...... ")

selection = input("You're at a crossroad. Where do you want to go? Type \"left\" or \"right\"").lower()

if selection=="left":
    lake_decesion = input("'You've come to a lake. There is an island in the middle of "
                          "the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.'").lower()
    if lake_decesion == "wait":
        door_decesion = input("You arrive at the island unharmed. There is a house with 3 doors. "
                              "One red, one yellow and one blue. Which colour do you choose?").lower()
        if door_decesion=="yellow":
            print(f"you won {player_name}")
        else:
            print(f"Game Over {player_name}")
    else:
        print(f"Game Over {player_name}")
else:
    print(f"Game Over {player_name}")
