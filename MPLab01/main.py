import pandas as pd
from math import acos, sin, cos, radians


def generate(numbers, K, start_index, current, result, method):
    if len(current) == K:
        result.append(current[:])
        return
    for i in range(start_index, len(numbers)):
        current.append(numbers[i])
        if method == "VR":
            generate(numbers, K, 0, current, result, "VR")
        elif method == "VWR" or method == "P":
            generate(numbers[:i] + numbers[i + 1:], K, 0, current, result, "VWR")
        elif method == "C":
            generate(numbers, K, i + 1, current, result, "C")
        current.pop()


def calc_distance(lat1, lat2, lon1, lon2):
    lat1, lat2, lon1, lon2 = map(radians, [lat1, lat2, lon1, lon2])
    return acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon2 - lon1)) * 6371


def calc_distance_lat(lat1, lat2):
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    dlat = lat2 - lat1
    return 6371 * abs(dlat)


def calc_distance_lon(lon1, lon2):
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    dlon = lon2 - lon1
    return 6371 * abs(dlon) * cos((lon1 + lon2) / 2)


def calc_shortest_dist(cities, K, N):
    variations = []
    numbers = cities["Id"].to_list()
    latitude = cities["Latitude"].to_list()
    longitude = cities["Longitude"].to_list()
    numbers = numbers[:N]
    generate(numbers, K, 0, [], variations, "VWR")

    smallest_distance = 99999999
    smallest_variation = []
    for variation in variations:
        temp_distance = 0
        for i in range(1, len(variation)):
            id1 = variation[i - 1] - 1
            id2 = variation[i] - 1
            lat1 = latitude[id1]
            lat2 = latitude[id2]
            lon1 = longitude[id1]
            lon2 = longitude[id2]
            temp_distance += calc_distance(lat1, lat2, lon1, lon2)

        if smallest_distance > temp_distance:
            smallest_distance = temp_distance
            smallest_variation = variation

    print("Shortest distance is ", smallest_distance, "km beetween: ")
    for i in smallest_variation:
        print(cities["Town"][i - 1])

    return


def calc_smallest_rectangle(cities, K, N):
    numbers = cities["Id"].to_list()
    latitude = cities["Latitude"].to_list()
    longitude = cities["Longitude"].to_list()
    combinations = []
    numbers = numbers[:N]

    generate(numbers, K, 0, [], combinations, "C")

    smallest_rectangle = 999999
    smallest_combination = []
    for combination in combinations:
        curr_latitudes = []
        curr_longitudes = []
        for i in combination:
            curr_latitudes.append(latitude[i - 1])
            curr_longitudes.append(longitude[i - 1])

        min_x, max_x = min(curr_latitudes), max(curr_latitudes)
        min_y, max_y = min(curr_longitudes), max(curr_longitudes)
        a = calc_distance_lat(min_x, max_x)
        b = calc_distance_lon(min_y, max_y)
        temp_rectangle = a * b
        if smallest_rectangle > temp_rectangle:
            smallest_rectangle = temp_rectangle
            smallest_combination = combination

    print("Smallest rectangle field is ", smallest_rectangle, "km^2 \nCities: ")
    for i in smallest_combination:
        print(cities["Town"][i - 1])

    return


N = 5  # liczba elementów
K = 3  # rozmiar podzbioru

numbers = [i for i in range(1, N + 1)]

variations_repeat = []
generate(numbers, K, 0, [], variations_repeat, "VWR")
print("Wariacje bez powtórzeń:", len(variations_repeat), " ", variations_repeat)
variations_repeat = []

combinations = []
generate(numbers, K, 0, [], combinations, "C")
print("Kombinacje:", len(combinations), " ", combinations)

cities = pd.read_csv("France.txt", sep=" ")
calc_shortest_dist(cities, K, N)
calc_smallest_rectangle(cities, K, N)
