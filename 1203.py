#verilen parayi az sayida bozuk para verecek sekilde geri donduren program

def myfunction(coin):
    temp = coin
    array = [50, 25, 21, 10, 5, 1]
    freq = [0, 0, 0, 0, 0, 0] #hangi paradan kac adet geldi
    counter = 0 #en az sayida olani bulmak icin
    minimum = coin

    for i in range(0,len(array)):
        for j in range(i,len(array)):
            while(temp//array[j] > 0):
                temp = temp-array[j]
                freq[j] += 1
                counter +=1
        if(counter<minimum):
            minimum = counter
            freq2 = freq
        freq = [0, 0, 0, 0, 0, 0]
        temp = coin
        counter = 0
    return freq2

print(myfunction(63))
            
