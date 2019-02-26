day=int(input("Which day of the year do you want to calculate?(0-365) "))

months=[31,28,31,30,31,30,31,31,30,31,30,31]
percent=100
i=0
while((day-months[i])>0 and i<12):
	day=day-months[i]
	i+=1

percent=day*5
if(percent>=100):
	percent=0
else:
	percent=100-percent

print "expectation: %",percent 
