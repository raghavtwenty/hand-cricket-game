
import random


def a():
    global f
    print('WELCOME TO HAND CRICKET GAME')
    print('MAN VS MACHNE')
    b = 1
    c = 2
    f = 0
    print('\n\t\tMACHINE WON THE TOSS, AND IT CHOSES TO CHASE.')
    a = 1
    if a == 1:
        print('YOU ARE BATTING. ALLOWED CHARACTERS 1 TO 5. NOT MORE THAN THAT.')
        while a == 1:
            print('==================================')
            d = int(input('\nUSER:BATTING:-  '))
            if d < 6:
                e = random.randrange(1, 6)
                print('MACHINE:BOWLING:- ', e)
                if (d != e):
                    f = f+d
                    print('\nYOUR SCORE: ', f)
                else:
                    print('\nxxxxxxx   USER OUT!   xxxxxxxx')
                    print("\nYOUR TOTAL SCORE: ", f)
                    break
            elif d > 5:
                print('INVALID INPUT.')
            else:
                print('INVALID INPUT.')


def b():
    global f1
    print('\n\n\t\tNOW YOUR ARE BOWLING.')
    g = 2
    h = 2
    f1 = 0
    if g == h:
        print('YOU ARE BOWLING. ALLOWED CHARACTERS 1 TO 5. NOT MORE THAN THAT.')
        while 2 == 2:
            print('==================================')
            i = int(input('\nUSER:BOWLING:-  '))
            if i > 6:
                print('\nINVALID INPUT.')
            else:
                j = random.randrange(1, 6)
                print('MACHINE:BATTING:- ', j)
                if (j != i):
                    f1 = f1+i
                    print('\nMACHINE SCORE:', f1)
                    if f1 > f:
                        print('\n-------MACHINE WON THE MATCH----------')
                        break
                elif j == i:
                    print('\nxxxxxxxx   MACHINE OUT!   xxxxxxx')
                    print('\nMACHINE TOTAL SCORE: ', f1)
                    break


a()
b()
if f == f1:
    print('\n------MATCH DRAW------')
elif f > f1:
    print('\n------YOU WON THE MATCH-----')
