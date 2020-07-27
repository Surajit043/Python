'''

while loop

while predicted :
      code

predicate ----> code -----> predicate ---> code -----> predicate -----> False ----> loop end

(condition true -----> code ) & (condition false -------> loop end )


'''

# infinite loop
# while True :
#    print ( 'hello world')


i = 0
while i < 5 :
    print (i)
    i = i+1   # i += 1

else :
    print ('i am outside loop')
