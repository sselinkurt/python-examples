
def my_Vectors_Inner_Product(v,w):
    size=len(v)
    my_result=[]
    for i in range(size):
        my_result.append(0)
    for i in range(size):
        my_result[i]=v[i]*w[i]

    t=0
    for i in range(size):
        t=t+my_result[i]

    return t

def my_Vector_Scalar_Product(alpha,v):
    size=len(v)
    my_result=[]
    for i in range(size):
        my_result.append(0)
    for i in range(size):
        my_result[i]=alpha*v[i]
    return my_result

def my_Vector_Substraction(v,w):
    size=len(v)
    my_result=[]
    for i in range(size):
        my_result.append(0)
    for i in range(size):
        t=t+my_result[i]
    return t

def my_Vector_Scalar_Product(alpha,v):
    size=len(v)
    my_result=[]
    for i in range(size):
        my_result.append(0)
    for i in range(size):
        my_result[i]=alpha*v[i]
    return my_result

def my_Vector_Substraction(v,w):
    size=len(v)
    my_result=[]
    for i in range(size):
        my_result.append(0)
    for i in range(size):
        my_result[i]=v[i]-w[i]
    return my_result

def my_Vector_Addition(v,w):
    size=len(v)
    my_result=[]
    for i in range(size):
        my_result.append(0)
    for i in range(size):
        my_result[i]=v[i]*w[i]
    return my_result

