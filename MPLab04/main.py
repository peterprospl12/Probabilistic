import random

xy = [[0 for _ in range(4)] for _ in range(4)]
def generator2():
    for i in range(100000):
        x = random.random()
        y = random.random()
        if x <= 0.5:
            x_index = 1
            if y <= 0.2:
                y_index = 1
            else:
                y_index = 4
        elif x <= 0.7:
            x_index = 2
            y_index = 1
        elif x <= 0.9:
            x_index = 3
            if y<= 0.5:
                y_index = 2
            else:
                y_index = 4
        else:
            x_index = 4
            y_index = 3
        xy[x_index-1][y_index-1] += 1

generator2()
for i in range(4):
    val = []
    for j in range(4):
        xy[i][j] = xy[i][j]
        val.append(xy[i][j])
    print(val)
