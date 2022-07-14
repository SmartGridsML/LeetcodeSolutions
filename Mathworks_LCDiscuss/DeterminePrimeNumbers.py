def isPrime(n):
    arr = [True] * (n+1)
    arr[0], arr[1] = False ,False
    #Sieve of erasthenes method
    for i in range(2, int(n**0.5 + 1)):
        if arr[i]:
            for j in range(i*i, n+1, i):
                arr[j] = False
    # Print list of primes up to N            
    # final = []
    # for i in range(2, max):
    #     if arr[i]:
    #         final.append(i)
    if(arr[n]):
        return arr[n]   
    else:
        return  

print(isPrime(1))
print(isPrime(14))
print(isPrime(17))
print(isPrime(18))
