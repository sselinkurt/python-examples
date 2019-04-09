#tersten okunusu ile ayni olan kelimeleri test eden fonksiyon

def sameWords(word):
    a = False
    if(word == word[::-1]):
        a = True
    return a

print(sameWords("selin"))
