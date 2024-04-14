from tabulate import tabulate
import sys
import csv

def get_distances():
    distances = []
    with open(r"C:\Users\ADMIN\Videos\Python_basics\routes_problem\distance.csv","r") as file:
        result = csv.reader(file)
        for item in result:
            distances.append(item)
    return distances

def get_routes():
    routes = []
    with open(r"C:\Users\ADMIN\Videos\Python_basics\routes_problem\routes.csv","r") as file:
        result = csv.reader(file)
        for item in result:
            routes.append(item)
    return routes

def get_stops_between_cities(cities,source,destination):
    for value in range(1,len(cities)):
        if source in cities[value][0] and destination in cities[value][0]:
            stops = [cities[value][1]]
    return stops

def sub_lists(city,distance):
    if city.issubset(distance):
        result = int([item for item in list(distance) if item.isdigit()==True ][0])
        return result
    return 0

def get_distance_between_stops(city_list,distances):
    result = city_list[0].split(",")
    i,sub_list,total_distance = 0,[],0
    for item in result:
        if i < len(result)-1:   # len=3  we want 0,1
            sub_list.append([result[i],result[i+1]])
            i+=1
    city_list = [set(item) for item in sub_list]
    cities_distances = [set(item) for item in distances]
    for item in city_list:
        for value in cities_distances:
            result = sub_lists(item,value)
            total_distance+=result
    return total_distance

def print_result(list1):
    print(tabulate(list1,headers=["SOURCE","DESTINATION","STOPS","DISTANCE(KM)"],tablefmt="grid"))

def display_distance_table(result3,start_city,end_city):
    result1 = get_stops_between_cities(result3,start_city,end_city)
    total_distance = get_distance_between_stops(result1,get_distances())
    print_result([[start_city,end_city,result1,total_distance]])

# get_cities_cli = sys.argv
# start_city = get_cities_cli[1]
# end_city = get_cities_cli[2]
# print(start_city," ",end_city)

display_distance_table(get_routes(),"Nagpur","Bangalore")