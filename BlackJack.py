import random

def start():
    i=int(input("Сколько игроков? 2,3,4\n"))
    if i==2:
        count=[0,0]
    elif i==3:
        count=[0,0,0]
    elif i==4:
        count=[0,0,0,0]

    koloda = [6,7,8,9,10,2,3,4,11] * 4
    random.shuffle(koloda)

    n=0
    while n<i:
        print("Ходит игрок номер %d"%(n+1))
        while True:
            choice = input('Будете брать карту? y/n\n')
            if choice == 'y':
                current = koloda.pop()
                print('Вам попалась карта достоинством %d' %current)
                count[n] += current
                if count[n] > 21:
                    print('У вас %d очков и вы проиграли'%count[n])
                    break
                elif count[n] == 21:
                    print('Поздравляю, вы набрали 21!')
                    break
                else:
                    print('У вас %d очков.' %count[n])
            elif choice == 'n':
                print('У {0} игрока {1} очков и вы закончили игру.'.format((n+1),count[n]))
                break
        n+=1
    res = 0
    chemp = 0
    n=0
    while n<i:
        if res<count[n] and count[n]<=21:
            res = count[n]
            chemp = n+1
        n+=1
    print("Игрок %d победил "%chemp)
    print('До новых встреч!')
    print('')

def game():
    while True:
        choice = input("Поиграем в блэкджек? y/n\n")
        if choice=="y":
            start()
        elif choice=="n":
            print("Good buy")
            break
game()