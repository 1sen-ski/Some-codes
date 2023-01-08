import random

acquired_letters1 = []
acquired_letters2 = []
acquired_letters3 = []

player1_points = 0
player2_points = 0
player3_points = 0

player1_turns = 0
player2_turns = 0
player3_turns = 0

player1 = input("Enter your name: ")
player2 = input("Choose player 2's name: ")
player3 = input("Choose player 3's name: ")

pl1_profile = {player1: " "}
pl2_profile = {player2: " "}
pl3_profile = {player3: " "}

am = "American"
de = "German"
fr = "French"

nationalities = int(input("\nPick a nationality(numbers 0 - 2, 0 being American, 1 being German and 2 being French): "))
if nationalities == 0:
    pl1_profile[player1] = am
elif nationalities == 1:
    pl1_profile[player1] = de
elif nationalities == 2:
    pl1_profile[player1] = fr
else:
    nationalities = int(input("Please pick a valid number: "))
if nationalities == 0:
    pl1_profile[player1] = am
elif nationalities == 1:
    pl1_profile[player1] = de
elif nationalities == 2:
    pl1_profile[player1] = fr
if nationalities != 0 and nationalities != 1 and nationalities != 2:
    quit("You *ucked up way too many times.")

pl2_profile[player2] = random.randint(0, 2)
pl3_profile[player3] = random.randint(0, 2)

if pl2_profile[player2] == 0:
    pl2_profile[player2] = am
elif pl2_profile[player2] == 1:
    pl2_profile[player2] = de
elif pl2_profile[player2] == 2:
    pl2_profile[player2] = fr

if pl3_profile[player3] == 0:
    pl3_profile[player3] = am
elif pl3_profile[player3] == 1:
    pl3_profile[player3] = de
elif pl3_profile[player3] == 2:
    pl3_profile[player3] = fr

list_pl1 = list(pl1_profile.values())
list_pl2 = list(pl2_profile.values())
list_pl3 = list(pl3_profile.values())

print("\nEveryone picked up their races, the game is about to begin!")
print("Current players are: ")
print(f"\nPlayer {player1} as {list_pl1[0]}.")
print(f"Player {player2} as {list_pl2[0]}.")
print(f"Player {player3} as {list_pl3[0]}.")

player_1_turns = input("\nGenerate the amount of turns you'll have for this game by pressing G: ")
if player_1_turns != "G".upper():
    quit("Wow how could you.")
elif player_1_turns == "G":
    player1_turns += random.randint(0, 5)

player2_turns += random.randint(0, 5)
player3_turns += random.randint(0, 5)

for gaming in range(player1_turns):
    stacks_1 = int(input("Pick a number between 0 and 7: "))
    if stacks_1 == 0:
        player1_points += 9
        acquired_letters1.append("A")
    elif stacks_1 == 1:
        player1_points += 1
        acquired_letters1.append("B")
    elif stacks_1 == 2:
        player1_points += 3
        acquired_letters1.append("C")
    elif stacks_1 == 3:
        player1_points += 3
        acquired_letters1.append("D")
    elif stacks_1 == 4:
        player1_points += 4
        acquired_letters1.append("E")
    elif stacks_1 == 5:
        player1_points += 7
        acquired_letters1.append("F")
    elif stacks_1 == 6:
        player1_points += 8
        acquired_letters1.append("G")
    elif stacks_1 == 7:
        player1_points += 2
        acquired_letters1.append("H")

for gaming in range(player2_turns):
    stacks_2 = random.randint(0, 7)
    if stacks_2 == 0:
        player2_points += 9
        acquired_letters2.append("A")
    elif stacks_2 == 1:
        player2_points += 1
        acquired_letters2.append("B")
    elif stacks_2 == 2:
        player2_points += 3
        acquired_letters2.append("C")
    elif stacks_2 == 3:
        player2_points += 3
        acquired_letters2.append("D")
    elif stacks_2 == 4:
        player2_points += 4
        acquired_letters2.append("E")
    elif stacks_2 == 5:
        player2_points += 7
        acquired_letters2.append("F")
    elif stacks_2 == 6:
        player2_points += 8
        acquired_letters2.append("G")
    elif stacks_2 == 7:
        player2_points += 2
        acquired_letters2.append("H")

for gaming in range(player3_turns):
    stacks_3 = random.randint(0, 7)
    if stacks_3 == 0:
        player3_points += 9
        acquired_letters3.append("A")
    elif stacks_3 == 1:
        player3_points += 1
        acquired_letters3.append("B")
    elif stacks_3 == 2:
        player3_points += 3
        acquired_letters3.append("C")
    elif stacks_3 == 3:
        player3_points += 3
        acquired_letters3.append("D")
    elif stacks_3 == 4:
        player3_points += 4
        acquired_letters3.append("E")
    elif stacks_3 == 5:
        player3_points += 7
        acquired_letters3.append("F")
    elif stacks_3 == 6:
        player3_points += 8
        acquired_letters3.append("G")
    elif stacks_3 == 7:
        player3_points += 2
        acquired_letters3.append("H")
print("\nGame End!")

print("\nStats: ")
print(f"Player {player1} got {player1_points} points and {acquired_letters1} letters.")
print(f"Player {player2} got {player2_points} points and {acquired_letters2} letters.")
print(f"Player {player3} got {player3_points} points and {acquired_letters3} letters.")

if player1_points > player2_points and player1_points > player3_points:
    print(f"Player {player1} has won with the most points!")
elif player2_points > player1_points and player2_points > player1_points:
    print(f"Player {player2} has won with the most points!")
elif player3_points > player2_points and player3_points > player1_points:
    print(f"Player {player3} has won with the most points!")

