import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.txt', header=None, sep="|", decimal=",")
print(data)


def arithmetic_mean(data):
    return sum(data) / len(data)


def default_moment(data, k):
    return sum([x ** k for x in data]) / len(data)


def central_moment(data, k):
    return sum([(x - arithmetic_mean(data)) ** k for x in data]) / len(data)


def standard_deviation(data):
    return (central_moment(data, 2)) ** 0.5


def average_deviations(data):
    return sum([abs(x - arithmetic_mean(data)) for x in data]) / len(data)


print("Arithmetic mean", arithmetic_mean(data[0]))
print("Default moment 2", default_moment(data[0], 2))
print("Central moment 1", central_moment(data[0], 1))
print("Central moment 2", central_moment(data[0], 2))
print("Standard deviation", standard_deviation(data[0]))
print("Average deviations", average_deviations(data[0]))
