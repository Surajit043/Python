'''
N
1 * 2 * 3 * ... * N
0! = 1
'''

# using While Loop
n =int(input( ))
m = 1
while n > 0 :
    m *= n
    n -= 1
print (m)


# using for loop
#k=1
#for i in range (1,n+1):
#    k *= i
#    print (k)
