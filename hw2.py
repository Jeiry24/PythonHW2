import random

#Task 10

n = random.randint(2,15)
coins = [random.randint(0,1) for _ in range(n)]
emblem = 0
tails = 0
for i in range (n):
    if coins[i] == 1:
        emblem += 1
    else:
        tails += 1
print("Орлов:",tails)
print("Решек:",emblem)
print("Минимальное количество монет,которые нужно перевернуть:",min(tails,emblem))


# Task 12
x, y = abs(int(input())), abs(int(input()))
s = x + y
p = x * y
check = 0
for i in range(1001):
    if check !=1:
        for j in range(1001):
            if check !=1:
                if i * j == p and i + j == s:
                    check = 1
                    print(i,j)

# Task 14

num = abs(int(input()))
k = 1
while (k * 2) < num:
    print(2 * k)
    k *= 2