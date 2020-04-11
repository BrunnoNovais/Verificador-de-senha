def func(TAMANHO=6):
    num = '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'
    letra = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
             'w', 'x', 'y', 'z']
    caracteres = ['!', '@', '#', '$', '%', '&', '*']
    SENHA_FINAL = []
    import random as rd
    T = len(SENHA_FINAL)
    while T != TAMANHO:
        pos1 = num[rd.randint(0, 5):rd.randint(6, 9):rd.randint(1, 3)]
        pos2 = letra[rd.randint(0, 5):rd.randint(6, 9):rd.randint(1, 3)]
        pos3 = caracteres[rd.randint(0, 5):rd.randint(6, 9):rd.randint(1, 3)]

        for c in pos1:
            SENHA_FINAL.append(c)

        for c in pos2:
            SENHA_FINAL.append(c)

        for c in pos3:
            SENHA_FINAL.append(c)

        rd.shuffle(SENHA_FINAL)

        T = len(SENHA_FINAL)

    print(SENHA_FINAL)
func()
