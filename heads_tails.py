import random

# Solution 1
# toss = ['Heads', 'Tails']
# print(random.choice(toss))

# Solution 2
random_num = random.randint(0, 1)

if random_num == 0:
    print("Heads")
else:
    print("Tails")