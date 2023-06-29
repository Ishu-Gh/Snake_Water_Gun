import random
def game(comp,you):
    if comp=='s':
        if you=='w':
            print("You loss and comp win -> computer choose ",comp)
        elif you=='g':
            print("You won and comp loss -> computer choose ",comp)
        elif you=='s':
            print("match tied")
    elif comp=='w':
        if you=='s':
            print("You won and comp loss -> computer choose ",comp)
        elif you=='g':
            print("You loss and comp won -> computer choose ",comp)
        elif you=='w':
            print("match tied")
    elif comp=='g':
        if you=='s':
            print("You loss and comp win -> computer choose ",comp)
        elif you=='w':
            print("You won and comp loss -> computer choose ",comp)
        elif you=='g':
            print("match tied")        

print("Comp turn: snake(s),water(w),gun(g)")
rand_no=random.randint(1,3)
# print(rand_no)

if rand_no==1:
    comp='s'
elif rand_no==2:
    comp='w'
elif rand_no==3:
    comp='g'        

you=input("your turn: snake(s),water(w),gun(g)\n")
game(comp,you)