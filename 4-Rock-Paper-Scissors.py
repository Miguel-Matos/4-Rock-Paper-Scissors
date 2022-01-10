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

#Write your code below this line 👇

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
options = [rock, paper, scissors]
ran_choice = random.randint(0, 2)

player_choice = options[choice]
enemy_choice = options[ran_choice]


if player_choice == options[0] and enemy_choice == options[0]:
    print(player_choice)
    print(enemy_choice)
    print("It's a tie!")
elif player_choice == options[0] and enemy_choice == options[1]:
    print(player_choice)
    print(enemy_choice)
    print("The enemy wins!")
elif player_choice == options[0] and enemy_choice == options[2]:
    print(player_choice)
    print(enemy_choice)
    print("You win!")
elif player_choice == options[1] and enemy_choice == options[0]:
    print(player_choice)
    print(enemy_choice)
    print("You win!")
elif player_choice == options[1] and enemy_choice == options[1]:
    print(player_choice)
    print(enemy_choice)
    print("It's a tie!")
elif player_choice == options[1] and enemy_choice == options[2]:
    print(player_choice)
    print(enemy_choice)
    print("You lose!")
elif player_choice == options[2] and enemy_choice == options[0]:
    print(player_choice)
    print(enemy_choice)
    print("You lose!")
elif player_choice == options[2] and enemy_choice == options[1]:
    print(player_choice)
    print(enemy_choice)
    print("You win!")
elif player_choice == options[2] and enemy_choice == options[2]:
    print(player_choice)
    print(enemy_choice)
    print("It's a tie!")

