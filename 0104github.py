#hash table

import random

def createMyHashTable(N): #N should be prime
    myTable = []
    for i in range(N):
        myTable.append(0)
    
    return myTable

def my_hash(size,numberToBeInserted):
    return numberToBeInserted%size

def insertMyHashTable(myTable,numberToBeInserted):
    isCollision = False
    index = my_hash(len(myTable),numberToBeInserted)
    if(myTable[index]==0): #yerlesmeye calistigin yer dolu
        myTable[index] = 1
    else:
        isCollision = True

    return isCollision
myhash1 = createMyHashTable(13)
print(myhash1)
print(insertMyHashTable(myhash1,17))
print(insertMyHashTable(myhash1,30))

def myTest(size=13,numberOfInsert=10):
    myhash1 = createMyHashTable(size)
    c = 0
    for s in range(numberOfInsert):
        #number = random.choice([0,1,2,3,4,5,6,7,8,9])
        number = random.randint(0,10000)
        if(insertMyHashTable(myhash1,number) == True):
            c = c+1
    return c #collision kac defa
print(myTest(703,50)) 
