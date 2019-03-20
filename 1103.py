#sayinin bolenlerini bulan, asal ise asal yazdiran program
liste = []
sayi = int(input("sayi giriniz:"))

def my_prime(sayi):
    if(sayi==2):
        print("ASAL")
    elif(sayi==1):
        print(1)
    for i in range(1,sayi+1):
        if(sayi%i==0):
            liste.append(i)
        if(i>sayi**(1/2) and len(liste)==1):
            print("ASAL")
            liste.append(sayi)
            break
    return liste
    
print("bölenler:", my_prime(sayi))

