import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
options_list = [rock, paper, scissors]

user_choice = int(input("Type 0 for rock, 1 for paper and 2 for scissors"))
computer_choice = random.randint(0,2)

if user_choice >=3 or user_choice < 0:
  print("Sorry, the number you type is not valid, YOU LOSE")
else:
  if user_choice == computer_choice:
    print(f"ITS A DRAW, you choose {options_list[user_choice]} and the computer choose {options_list[computer_choice]}")
  elif user_choice == 0 and computer_choice == 2:
    print(f"YOU WIN, you choose {options_list[user_choice]} and the computer choose {options_list[computer_choice]}")
  elif user_choice == 1 and computer_choice == 0:
    print(f"YOU WIN, you choose {options_list[user_choice]} and the computer choose {options_list[computer_choice]}")
  elif user_choice == 2 and computer_choice == 1:
    print(f"YOU WIN, you choose {options_list[user_choice]} and the computer choose {options_list[computer_choice]}")
  else:
    print(f"YOU LOST, you choose {options_list[user_choice]} and the computer choose {options_list[computer_choice]}")