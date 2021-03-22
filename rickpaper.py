import random
var = {'scissors': 1,'paper': 2,'rock': 0}
user = input("Please choice scissors, paper or rock: ")
while user not in ['scissors', 'paper', 'rock']:
    user = input("Please choice scissors, paper or rock: ")
computer = random.choice(['scissors', 'paper', 'rock'])
print(f"USER - {user} \nCOMPUTER - {computer}")
one = var[user]
two = var[computer]
if (one < two and abs(one - two) == 1) or (one > two and abs(one - two) == 2):
    print(f"USER with {user} - WIN!")
elif one == two:
    print("==TIE==")
else:
    print(f"COMPUTER with {computer} - WIN!")