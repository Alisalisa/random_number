from random import randint

random_number = randint(1, 100)

utilizator = raw_input('Cum va numiti?\n')

print '%s, sa incepem!'%utilizator

file = open("file.txt", "a+")

file.write(utilizator)
file.write(" ")
y_number = 0
incercari = 0

while (y_number != random_number):
    your_number = raw_input('Introduceti un numar de la 1 la 100: ')
    incercari = incercari + 1
    try:
        y_number = int(your_number)
        if (random_number == y_number):
            if (incercari == 1):
                print 'Ati ghicit numarul din prima incercare. Felicitari!\n'
            else:
                print 'Ati ghicit numarul din a %d-a incercare!\n'%incercari
        elif (random_number > y_number):
            print 'Numarul introdus e prea mic. Incercati un numar mai mare.\n'
        else:
            print 'Numarul introdus e prea mare. Incercati un numar mai mic.\n'
    except:
        print 'Trebuie sa introduceti doar cifre!'

str_incercari = str(incercari)
file.write(str_incercari)
file.write(" ")
file.write("\n")

file.close()

file = open("file.txt", "a+")
str = 'a'
i = 0
incercari_utilizator = []

while (str != ''):
    str = file.readline()
    if utilizator in str:
        numar = str.split(" ")[1]
        incercari_utilizator.append(numar)
        i = i + 1
    
print 'Este a %d-a oara cand va jucati. Rezultatele dumneavoastra sunt:'%i

for n in incercari_utilizator:
    print n
    
file.close()

file = open("file.txt", "a+")

raspuns = 'da'

while (raspuns == 'da'):
    raspuns = raw_input('Doriti sa cautati rezultatele unui alt utilizator? (Scrieti "da" daca doriti, si orice altceva daca nu): ')
    str = 'a'
    inc_util = []
    j = 0

    if (raspuns == 'da'):
        util = raw_input('Scrieti numele utilizatorului cautat: ')
        while (str != ''):
            str = file.readline()
            if util in str:
                num = str.split(" ")[1]
                inc_util.append(num)
                j = j + 1
        if (j != 0):
            print 'Utilizatorul s-a jucat de %d ori. Rezultatele lui sunt:'%j
        elif (j == 0):
            print 'Utilizatorul cautat nu s-a jucat niciodata.\n'
        for n in inc_util:
            print n

file.close()