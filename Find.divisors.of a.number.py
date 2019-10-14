"""
Task...

    Find the number of divisors of a positive integer n.
    Random tests go up to n = 500000.
    Examples
    divisors(4)  = 3  # 1, 2, 4
    divisors(5)  = 2  # 1, 5
    divisors(12) = 6  # 1, 2, 3, 4, 6, 12
    divisors(30) = 8  # 1, 2, 3, 5, 6, 10, 15, 30
"""
def divisors(n):
    count = 0
    for numer in range(n):
        var = divmod(n,numer+1)
        if(var[1] == 0):
            count += 1
    return count

print("Calling the function....")

print("The divisor function returns : " + str(divisors(4)))

"""
Created by...

    Jesus Lopez Mesia (https://www.linkedin.com/in/susejzepol/)

At date...
    
    2019-10-14
"""