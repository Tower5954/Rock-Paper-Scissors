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

weapon = [rock, paper, scissors]

player_weapon = int(input("What do you choose? Type 0 for ROCK, 1 for PAPER, or 2 for SCISSORS\n "))

print(weapon[player_weapon])

cpu_weapon = random.randint(0,2)
print("Meet your doom! The computer picks...")
print(weapon[cpu_weapon])

if player_weapon >= 3:
  print("You Lose!")
if player_weapon == 0 and cpu_weapon == 2:
  print("You got lucky this time jerk!")
elif cpu_weapon == 0 and player_weapon == 2:
  print("Jerk-off you lose, HA HA No one can beat the invincible Laptop of Death")
elif cpu_weapon > player_weapon:
  print("HA HA HA Beat it A-Hole!")
elif player_weapon > cpu_weapon:
  print("BAAAAH You cheated!!! You cant beat me! best out of 3!???")
elif cpu_weapon == player_weapon:
  print("lucky, lucky but not next time punk!")
elif player_weapon >= 3:
  print("Nice try dickwad go play with the traffic!")

  
