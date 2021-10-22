import random
import time

# def random_pop(data):
#     number=random.randint(0,len(data)-1)
#     return data.pop(number)

def random_pop(data):
    number=random.choice(data)
    data.remove(number)
    return number

if __name__=="__main__":
    data=[1,2,3,4,5]
    while data:
        print(random_pop(data))
        time.sleep(1)

#print(random_pop())