import random
import matplotlib.pyplot as plt
import numpy as np
import pylab


def generator2():
    numbers = [0, 0, 0, 0]
    for i in range(100000):
        x = random.random()
        if x < 0.2:
            numbers[0] += 1
        elif x < 0.6:
            numbers[1] += 1
        elif x < 0.9:
            numbers[2] += 1
        elif x < 1.0:
            numbers[3] += 1
    for i in range(1, 5):
        numbers[i-1] = numbers[i - 1] / 100000
        print(str(i) + " | Prob: " + str(numbers[i - 1]))
    print()
    return numbers


def divide(number):
    return 1/100 * number


# y = (x-50)*(1/100)
# 100y = x-50
# x = 100y + 50
def generate1():
    arg = [0]*10
    for i in range(100000):
        y = random.random()
        x = 100*y + 50
        for j in range(10):
            if 50.0 +j*10 < x <= 60.0+j*10:
                arg[j] += 1
                break
    for i in range(10):
        print("[", (50+i*10), '-', (60+i*10), ']', arg[i])
    return arg



numbers = generator2()
numbres1 = generate1()
xpoints = np.array([0, 1, 2, 3, 4])
ypoints = [0]

for i in range(len(numbers)):
    ypoints.append(numbers[i] + ypoints[i])
plt.plot(xpoints, ypoints)
pylab.show()


xpoints = [i*10 for i in range(5,5+len(numbres1))]
ypoints = [numbres1[i] for i in range(len(numbres1))]
plt.plot(xpoints, ypoints)
pylab.show()