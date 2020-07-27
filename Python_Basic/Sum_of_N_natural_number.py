'''
sun of N natural number
1+2+3+4.......+N
'''

number = int(input( ))
j = 0
for i in range (0,number+1):
    j = j+i
    i += 1
print ( j )

# using while Loop
k=0
sum = 0
while k <= number :
    sum += k
    k +=1
print (sum)

# Efficient code
x = (number * (number +1)/2)
print (x)
