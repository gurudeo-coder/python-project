import random

while True:
    print("1. ro the dyce   2. exit")
    user = int(input("what id your choice from above ? "))
    
    if user == 1:
        number = random.randint(1,6)
        print(number)
        print("---------------")

    else:
        break
