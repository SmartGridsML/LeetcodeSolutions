"""
You are given an array people where people[i] is the weight of the ith person,
and an infinite number of boats where each boat can carry a maximum weight of limit.
Each boat carries at most two people at the same time, provided the sum of the weight
of those people is at most limit.

Return the minimum number of boats to carry every given person.
"""

def numRescueBoats( people: list[int], limit: int) -> int:
    output = 0
    #return  output
    i , j = 0, len(people)-1
    while(i <= j):
        
        ans +=1
        if(people[i] + people[j] <= limit):
            i+=1
        j -=1
    return output

def factorial(n):
    """ returns n!"""
    return 1 if n<2 else n*factorial(n-1)

fact = factorial
ls = [fact(i) for i  in range(11)]
print(ls)