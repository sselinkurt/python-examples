#toplamkilo agirlik miktarina kadar alabilecegi en degerli esyalari bulunuz

class Item(object):
    def __init__(self, n, v, w, o):
        self.name=n
        self.value=v
        self.weight=w
        self.oran=o

def steal(toplamkilo):
    item1=Item('Vase', 50, 2, 25)
    item2=Item('clock', 175, 10, 17.5)
    item3=Item('Computer', 200, 20, 10)
    item4=Item('Painting', 90, 9, 10)
    item5=Item('Book', 10, 1, 10)
    item6=Item('Radio', 20, 4, 5)
    items = [item1, item2, item3, item4, item5, item6]

    kilo = 0
    deger = 0
    maxdeger = 0
    array = []
    array2 = []

    for i in range(0, len(items)):
        if(items[i].weight <= toplamkilo):
            kilo = items[i].weight
            deger = items[i].value
            array.append(items[i].name)
        for j in range(i+1, len(items)):
            if(kilo+items[j].weight <= toplamkilo):
                deger += items[j].value
                kilo += items[j].weight
                array.append(items[j].name)
        if(deger > maxdeger):
            maxdeger = deger
            array2 = array.copy()
        kilo = 0
        deger = 0
        array.clear()
    return array2, maxdeger
print(steal(20))
    

