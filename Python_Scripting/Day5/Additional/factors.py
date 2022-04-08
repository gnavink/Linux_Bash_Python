def factors(n) :
    Factorlist = [ ]
    for i in range(1,n+1):
        if n%i == 0:
            factorlist = factorlist + [i] 
        return(factorlist)


def isprime(n): 
    return(factors(n) == [1,n])


def nprimes(n): 
    (count,i,plist) = ( 0,1,[ ] )
    while(count < n): 
        if isprime(i): 
            (count,plist) = (count+1,plist+[i]) 
        i = i+1 
    return(plist)

def primesupto(n): 
    Primelist = [ ] 
    for i in range(1,n+1): 
        if isprime(i): 
            primelist = primelist + [i] 
    return(primelist)

if __name__ == '__main__':
  
  print( factors(17) ==  [1,17] )
  print (factors(18) == [1,2,3,6,9,18] )

