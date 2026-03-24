import random

def dice():
    return random.randint(1,6)

if __name__ == '__main__':
    for atempts in range(10,100,10):
        number = {1:0,2:0,3:0,4:0,5:0,6:0}
    for _ in range(atempts):
        n = dice()
        number[n] += 1
    print(number)

    for _ in range(1000):
        pass
