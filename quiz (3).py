#melissa
#01/09

#init
import time
import random
score = 0
#function

#main

def multi_quiz():
    global score
    while True:

        print("Welcome to the Multiplication Quiz")
        question = int(input("How many questions?"))
        difficulty = (input("What level of difficulty? easy? medium? hard?"))
        start_time = time.time()
        print("Question 1 of 5")
        if difficulty == "easy":
            for i in range(question):
                num1 = random.randint(1,10)
                num2 = random.randint(1,10)
                print("what is " +  str(num1) + " times " + str(num2))
                answer = int(input("Enter answer: "))
                if answer == num1 * num2:
                    print("correct!")
                    score = score + 1
                else:
                    print("wrong, try again")
                    score = score + 0
        elif difficulty == "medium":
            for i in range(question):
                num1 = random.randint(1,20)
                num2 = random.randint(1,20)
                print("what is " +  str(num1) + " times " + str(num2))
                answer = int(input("Enter answer: "))
                if answer == num1 * num2:
                    print("correct!")
                    score = score + 1
                else:
                    print("wrong, try again")
                    score = score + 0
        elif difficulty == "hard":
                for i in range(question):
                    num1 = random.randint(1,50)
                    num2 = random.randint(1,50)
                    print("what is " +  str(num1) + " times " + str(num2))
                    answer = int(input("Enter answer: "))
                    if answer == num1 * num2:
                        print("correct!")
                        score = score + 1
                    else:
                        print("wrong, try again")
                        score = score + 0
        print("you got " + str(score) + " of " + str(question) + " correct ")
        end_time = time.time()
        elapsed_time = end_time - start_time
        print("you completed quiz in " + str(elapsed_time) + " Seconds")


        playagain = input("Do you want to play again")
        if playagain == "yes":
            print("restarting...")
        else:
            print ("Thank you. Bye.")
            break


multi_quiz()


