import random

def generatePass():
    with open('words.py', 'r') as document:
        words = document.readlines()
        x = words[int(random.randrange(0, len(words)))]
        y = words[int(random.randrange(0, len(words)))]
        z1 = random.randrange(0, 9)
        z2 = random.randrange(0, 9)

    document.close()

    pwd = str(x.capitalize()) + str(y.capitalize()) + str(z1) + str(z2)
    
    return pwd