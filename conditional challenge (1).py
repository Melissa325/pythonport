#conditionals statements

#init
#function
#challege

#18 years of age or older
#U.S. Citizen

def vote_check():
    age = int(input("please enter your age: "))
    citizen = input("are you a citizen(yes, no): ")
    if age >= 18 and citizen == "yes":
        print(" you can vote ")
    else:
        print("you are not eligible")

def max_num(a,b,c):
    if a > b and a > c:
        print("A is the largets number, the value of a is: " + str(a))
    if b > a and b > c:
        print("B is the largest number, the value of b is: " + str(b))
    if c > a and c > b:
        print("C is the largest number, the value of c is: " + str(c))

def score_to_grade(score):
    if score >= 90:
        print("A")
    elif score >= 80:
        print ("B")
    elif score >= 70:
        print ("C")
    elif score >= 60:
        print ("D")
    elif score <= 60:
        print ("F")

#main
score_to_grade(76)
