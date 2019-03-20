#listedeki ardisik elemanlari toplayip max sonucu veren program

arr=[4, -3, 2, -1, -2, 6, -5]

def max_sum(array):
    sayi = 0
    enbuyuk = 0
    for i in range(len(array)):
        for j in range(i, len(array)):
            sayi += array[j]
            if(sayi>enbuyuk):
                enbuyuk = sayi
        sayi = 0
    return enbuyuk
print(max_sum(arr))
    
