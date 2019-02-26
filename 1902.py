
def fibonacci_loop(n):
	a,b=0,1
	if(n==0):
		return 0
	for i in range(n-1):
		a,b=b,a+b
	return b

#print(fibonacci_loop(5))

def fibonacci_recursive(n):
	if(n<2):
		return n
	else:
		return fibonacci_recursive(n-1)+fibonacci_recursive(n-2)
#print(fibonacci_recursive(4)) 



def factorial(n):
	s=1
	for i in range(1,n+1):
		s=s*i
	return s
#print(factorial(4))

def factorial_recursive(n):
	if(n==0):
		return 1
	if(n==1):
		return 1
	else:
		return n*factorial_recursive(n-1)
#print(factorial_recursive(2))

def power(m,n):
	s=m
	for i in range(1,n):
		s=s*m
	if(m==0):
		s="tanimsiz"
	return s
	
#print(power(6,2))

def power_recursive(m,n):
	if(n==0):
		return 1
	elif(m==0):
		return "tanimsiz"
	elif(n==1):
		return m
	elif(n%2==0):
		return power_recursive(m*m,n//2)
	elif(n%2!=0):
		return power_recursive(m*m,(n//2))*m

#print(power_recursive(4,1))


