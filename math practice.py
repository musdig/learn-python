import random



def question():

    attempts = 4
    ca = 0
    while attempts > 0:
        a = random.choice(range(1, 10))
        b = random.choice(range(1, 10))
        d= a + b
        print(str(a)+ "+" + str(b))
        c = int(input("What is your answer"))
        if d==c:
            ca = ca +1
            print(d)
            print("you are right")
        else:
            print("you are wrong")
        attempts = attempts - 1
        print("that was attempt no."+ str((attempts)))
    print("you got " + str(ca) + " out of 10")

question()