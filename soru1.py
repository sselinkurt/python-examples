def syllableInSentences(text, string):
    array = [] #string in baslangic indislerini tuttugum dizi
    a = False
    length = len(text)
    for i in range(length):
        for j in range(length, -1, -1):
            if(text[i:j] == string):
                array.append(i+1)
                a = True
    return a,array
print(syllableInSentences("onsekiz mart art ","art"))

