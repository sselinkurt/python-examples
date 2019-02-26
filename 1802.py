#selection sort
my_arr=[21,12,13,44,25,2,7,16,14,35]

def mysearchSelection(my_array):

	for i in range(len(my_array)-1,0,-1):
		positionOfMax=0
		for location in range(1,i+1):
		#	print("j: ",location,"i :",i, end="\n")
			if(my_array[location]>my_array[positionOfMax]):
				positionOfMax=location
		temp=my_array[location]
		my_array[location]=my_array[positionOfMax]
		my_array[positionOfMax]=temp

		
mysearchSelection(my_arr)
print(my_arr)


#binary search
#midpoint is the middle number of the array
#s represent the number of swap

def my_binary_search(my_sorted_array,item):
	first=0
	last=len(my_sorted_array)-1
	found=False
	s=0
	while first<=last and not found:
		midpoint=(first+last)//2   
		s=s+1
		if(my_sorted_array[midpoint]==item):
			found=True
		else:
			if(item<my_sorted_array[midpoint]):
				last=midpoint-1
			else:
				first=midpoint+1
	return found,midpoint,s

#print(my_binary_search(my_arr,16))
#print(my_binary_search(my_arr,43))



