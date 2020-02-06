def add(num1,num2):
    return num1+num2


def isprime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count=count+1
    print("number of factors for",n,"is",count)
    if count==2:
        print(n,"is a prime")
    else:
        print(n,"is not prime")
       
    
def evod(s,e):
    for i in range(s,e+1):
        if i%2==0:
            print(i,"is even")
        else:
            print(i,"is odd")
            
            
    
def even(s,e):
    for i in range(s,e+1):
        if i%2==0:
            print(i,"is even")
            
            
def fact(n):
    if n==1:
        return 1
    else:
        return(n*fact(n-1))

            
