

def hash(s):
    '''
    Описание функции hash.
    функция создвет хэш

    s = строка которая поступает на вход
    с = полученный хэш


    '''
    letter = 'abcdefghijklmnopqrstuvwxyz'
    letter = letter + letter.upper()
    letter += '0123456789'
    p = 65
    m = 10**9 + 9
    c = 0 
    for i in range(len(s)):
        c += (letter.index(s[i]) + 1) * p**i % m

    return c 



