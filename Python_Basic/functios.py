"""
Functions
def function_name(arg1, arg2, arg3 ....):
    code
    code
    return val1, val2, val3 ... (not compulsory)
"""
#def helloworld ( ):
#    print ('hello world')
#    print (' hello i am there')

# deficult parameter
def fullName(firstName, lastName, middleName=' '):
    if middleName:
        print(firstName + ' ' + middleName + ' ' + lastName)
    else:
        print(firstName + ' ' + lastName)

fullName('john', 'doe')
fullName('anish', 'sachdeva')
fullName('wolfgang', 'mozart', 'amadeus')
