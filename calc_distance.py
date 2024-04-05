import json
from tabulate import tabulate
import sys

def get_distances():
    with open(r"C:\Users\ADMIN\Videos\Python_basics\routes_problem\distance.json","r") as file:
        result = json.load(file)
    return result

def get_routes():
    with open(r"C:\Users\ADMIN\Videos\Python_basics\routes_problem\routes.json","r") as file:
        result = json.load(file)
    return result

def get_stops_between_cities(cities,source,destination):
    for item in cities:
        if item["from"] == source and item["to"] == destination or item["to"] == source and item["from"] == destination:
            stops = item["stops"]
            all_stops = stops.split(" ")
    return all_stops

def get_distance_between_stops(city_list,distances):
    total_distance = 0
    for item in distances:
        for i in range(len(city_list)):
            if i < len(city_list) - 1:
                if city_list[i] == item["from"] and city_list[i+1] == item["to"] or city_list[i] == item["to"] and city_list[i+1] == item["from"]:
                    total_distance += item["distance"]
    return total_distance

def print_result(list1):
    print(tabulate(list1,headers=["SOURCE","DESTINATION","STOPS","DISTANCE(KM)"],tablefmt="grid"))

def display_distance_table(result3,start_city,end_city):
    result1 = get_stops_between_cities(result3,start_city,end_city)
    if result1 == [""]:
        result = get_distances()
        for item in result:
            if start_city == item["from"] and end_city == item["to"] or start_city == item["to"] and end_city == item["from"] :
                distance = item["distance"]
        print_result([[start_city,end_city,[],distance]])
    else:
        total_distance = get_distance_between_stops(result1,get_distances())
        print_result([[start_city,end_city,result1,total_distance]])

get_cities_cli = sys.argv
start_city = get_cities_cli[1]
end_city = get_cities_cli[2]
print(start_city," ",end_city)

display_distance_table(get_routes(),start_city,end_city)