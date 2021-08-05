# other ways to creating sequence of head's and tail's
import random
def coin_toss (N) :
    h = 0              #Initating for head count
    H = []              #Empty list
    for i in N :
        h += random.choice([0,1])
        H.append(h/i)       #fraction Append
    return (H)