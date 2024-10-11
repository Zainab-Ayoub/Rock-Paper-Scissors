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

# list = [[rock], [paper], [scissors]]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors."))
print(f"You chose: {user_choice}")
computer_choice = random.randint(0,2)
print(f"Computer chose: {computer_choice}")

if user_choice >=3 or user_choice < 0:
    print("You typed an invalid number, you lose!") 
elif user_choice == 0 & computer_choice == 2:
    print("You win!")
elif user_choice == 2 & computer_choice == 0:
    print("You lose")    
elif user_choice < computer_choice:
    print("You lose")    
elif user_choice > computer_choice:
    print("You win!")    
elif user_choice == computer_choice:
    print("It's a draw!")    
     
    