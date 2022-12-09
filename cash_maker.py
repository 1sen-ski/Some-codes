import time
import random
money = 0
repetitions = 3000
print("That's the inflation inducing machine, boy.")
for cash in range(0, repetitions, 1):
    time.sleep(2)
    the_easy_money = random.randint(20, 500)
    print(f"Added cash right now: {the_easy_money}$")
    money += the_easy_money
    print(f"Total cash: {money}$")
    if money >= 400:
        print(f"Yep, that's enough, now we can buy the guns and proceed with our good deeds!!")
        print(f"Balance: {money}$")
        quit()