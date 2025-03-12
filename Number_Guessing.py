import random
def random_game():
    a = random.randint(0,20)
    attempts = 5
    
    while attempts > 0:
        guess = int(input("ENTER GUESS:"))
        
        if  0 <= guess <= 20:
            if guess < a:
                print("Too Low")
            elif guess > a:
                print("Too High")
            else:
                print("Correct")
        else:
            print("Invalid Number")
        attempts -= 1
    if attempts == 0:
        print ("Game Over")

random_game()  
