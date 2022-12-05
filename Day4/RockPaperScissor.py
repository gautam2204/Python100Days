# Rock wins against scissors;   0
# paper wins against rock;      1
# scissors wins against paper   2
import random

rock = '''                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\'
'''

paper = ''' _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|              '''

scissors = '''
   ____
  / __ \
 ( (__) |___ ___
  \________,'   """""----....____
   _______<  () dd       ____----'
  / __   __`.___-----""""
 ( (__) |
  \____/
'''
list_with_choices = [rock,paper,scissors]

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for scissor\n"))
'''
if your_choice < 0 or your_choice >=3:
    print("Not a valid choice")
'''

print(f"Your choice {your_choice}")
print(list_with_choices[your_choice])

computer_choice = random.randint(0,2)
print(f"Computer chose {computer_choice}")
print(list_with_choices[your_choice])
# Rock wins against scissors;   0
# paper wins against rock;      1
# scissors wins against paper   2
if your_choice 



