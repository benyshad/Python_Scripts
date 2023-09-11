import random

def main():
    professor()

def professor():
    level = 0

    # prompt user for level between 1-3 and confirm that its a digit
    while True:
        level = input("Choose a level between 1 - 3: ")
        try:
            level = int(level)
            if level > 0 and level < 4:
                break    
            else:
                pass       
        except ValueError:
            pass
    # pass level to get_ints function
    get_ints(level)

# genarate 2 random numbers 10 times and each time pass the generated numbers to gen_prob function
def get_ints(level):
    score = 5

    for i in range(5):
        if level == 1:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
        elif level == 2:
            x = random.randint(10, 99)
            y = random.randint(10, 99)
        elif level == 3:
            x = random.randint(100,999)
            y = random.randint(100,999)
        # pass digits and score to gen_prob function    
        score = gen_prob(x,y, score)
    print("Score: " + str(score))
        

# genarate a math problem with the numbers provided for the user and check their answer
def gen_prob(x,y, score):
    # prompt user with problem 3 times
    for i in range(3):
        user_ans = input(str(x)+" + "+str(y)+ "? ")
        while True:
            if user_ans.isdigit == False or user_ans == "":
                user_ans = input(str(x)+" + "+str(y)+ "? ")
            else:
                break
        # pass var to check_ans func and check answer and the check_ans func returns a bool
        if check_ans(x,y,user_ans):
            return score
        else:
            print("EEE")

    # if user still has not given a correct answer then print the correct answer
    if check_ans(x,y,user_ans) == False:
        print(str(x)+" + "+str(y)+ " = " + str(x+y))
        score = score - 1
        return score

# check the answer and return a bool
def check_ans(x,y,user_ans):
    return int(user_ans) == x + y

if __name__ == "__main__":
    main()
