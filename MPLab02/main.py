from collections import deque
from math import *


class LinearGenerator:
    def __init__(self, a, c, m):
        self.a = a
        self.c = c
        self.m = m
        self.summ = 4

    def __generate__(self):
        x = (self.a * self.summ + self.c) % self.m
        self.summ = x
        return x / self.m


linear_generator = LinearGenerator(16807, 0, 2 ** 31 - 1)

counterf = 0
temp = []
for i in range(1000):
    x = linear_generator.__generate__()
    temp.append(x)
    if 0.1 <= x <= 0.25:
        counterf += 1

print(temp)
print("Sprawdzenie liniowego: ", counterf / 1000)

r = 1
R = 1
pointCounter = 0
circleCounter = 0
for i in range(100000):
    x, y = linear_generator.__generate__(), linear_generator.__generate__()
    x *= 2
    y *= 2
    x -= 1
    y -= 1

    dist1 = sqrt((x - 0.0) ** 2 + (y - 0.0) ** 2)
    dist2 = sqrt((x - 1.0) ** 2 + (y - 1.0) ** 2)
    if dist1 < 1.0:
        circleCounter += 1
    if dist1 < 1.0 and dist2 < R:
        pointCounter += 1

print("Eksperyment", pointCounter / 25000)
print("PI", circleCounter / 25000)


class RegisterGenerator:
    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.current_i = p + 1
        self.queue = deque([])
        linear_generator1 = LinearGenerator(16.807, 0, 2 ^ 31 - 1)

        for i in range(self.current_i + 1):
            x = linear_generator1.__generate__()
            if x > 0.5:
                self.queue.append(0)
            else:
                self.queue.append(1)

    def __generate__(self):
        bi = self.queue[self.current_i - self.p] ^ self.queue[self.current_i - self.q]
        self.queue.append(bi)
        self.queue.popleft()
        return bi


register_generation = RegisterGenerator(132049, 33912)

counterf = 0
temp = []
for i in range(1000):
    x = register_generation.__generate__()
    temp.append(x)
    if x == 1:
        counterf += 1

print(temp)
print("Sprawdzenie rejestrowego: ", counterf / 1000)

counter = 0
N = 20
K = 5
for i in range(100000):
    counterx = 0
    for j in range(N):
        x = register_generation.__generate__()

        if x == 1:
            counterx += 1
        else:
            counterx = 0

        if counterx >= K:
            counter += 1
            break

print("Eksperyment", counter / 100000)
