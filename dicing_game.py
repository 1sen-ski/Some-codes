import random
import time

print("Добре дошъл в Dicing Game, \nв играта ще въртиш 2 зара, според"
      " това какво ти се падне твоя баланс \nще се увеличава или намаля, при врътка с"
      " 2 шестици или 2 петици, получаваш Jim Beam Whisky 50ml")
roll_again = "да"
jim_beam_whisky_ml_counter = 0
profit = 0
lost_money = 0
name_of_user = input("Играч: ")
balance_of_user = int(input("Въведи си парите, които ще вложиш: "))
while roll_again == "да":
    print("\nЗара се върти...")
    time.sleep(1)

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print("Стойностите са: ")
    print(f"Зар 1 = {dice1}\nЗар 2 = {dice2}")

    if dice1 == 6 and dice2 == 6:
        jim_beam_whisky_ml_counter += 200
    elif dice1 == 5 and dice2 == 5:
        jim_beam_whisky_ml_counter += 50
        profit += 80
    elif dice1 == 4 and dice2 == 4:
        profit += 70
    elif dice1 == 3 and dice2 == 3:
        profit += 50
    elif dice1 == 2 and dice2 == 2:
        profit += 30
    elif dice1 == 1 and dice2 == 1:
        lost_money += 100
    if dice1 != dice2:
        lost_money += 25
    roll_again = input("\nЩе въртим ли още? (да/не): ")
    if roll_again == "не":
        break
balance_of_user = balance_of_user + profit
balance_of_user = balance_of_user - lost_money
while roll_again == "не":
    print(f"Баланса на {name_of_user} е {balance_of_user}лв.")
    print(f"Загубата е: {lost_money}")
    print(f"Временна спечелена сума: {profit}")
    print(f"Тотален милитраж на Jim Beam: {jim_beam_whisky_ml_counter} мл. уиски.")
    break
