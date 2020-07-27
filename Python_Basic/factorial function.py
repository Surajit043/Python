def factorial (number):
    result =1
    for i in range (1,number+1):
        result *= i
    return (result)
number = int (input())

print (factorial(number))
# permutation
def permutation (n,r):   # fac (n)/fac(n-r)
    return (factorial(n)/factorial (n-r))
n = int (input ( ))
r = int(input( ))
print (permutation(n,r))

# combination
def combination (n,r):    # nCr = n!/r! *(n-r)! ----> nPr/r!
    return (permutation (n,r)/factorial (r))
print (combination(n,r))


