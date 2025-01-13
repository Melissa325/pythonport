
#10/16

print("Welcome to your TV Show 2000")
print("Answer the questions to find out your TV Show")

def what_tvshow():
    ans = input("red (red) or green (green) ?")
    if ans == "red":
        ans = input("spring (spring) or summer (summer)?")
        if ans == "spring":
            ans = input("comedy (comedy) or romance (romance) genre?")
            if ans == "comedy":
                print("Your tv show is The offcice")
            else:
                print("your tv shows is How I met your Mother")
        else:
            ans = input("reality (reality) or teen (teen) genre?")
            if ans == "reality":
                print("your tv show is Jersey Shore")
            else:
                print("your tv show is Thats 70 show")
    else:
        ans = input("winter (winter) or fall (fall)?")
        if ans == "winter":
            ans = input("drama (drama) or animation (animation) genre?")
            if ans == "drama":
                print("your tv show is Greys Anatomy")
            else:
                print("your tv show is South Park")
        else:
            ans = input("friendship (friend) or crime (crime) genre?")
            if ans == "friend":
                print("your tv show is Friends")
            else:
                print("your tv show is Criminal Minds")





what_tvshow()

