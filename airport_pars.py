import csv


with open('airport.csv', mode='r', encoding='utf-8') as file:
    airport_data = file.readlines()
    for airport in airport_data:
        list_of_airports = airport.split(';')
        if list_of_airports[5] == 'UA':
            print(list_of_airports[2], list_of_airports[5])

