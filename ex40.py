cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville'}

cities['NY'] = 'New York'  #向字典里添加新的内容时，默认时新添加到字典末尾。 
cities['OR'] = 'Portland'

def find_city(themap, state):
    if state in themap:
        return themap[state]
    else:
        return "Not found."

# ok pay attention!
cities['_find'] = find_city #在字典中，可以存入函数
print(cities)

while True:
    print("State? (ENTER to quit)",)
    state = input(">")

    if not state:
        break

    #this line is the most important ever! study!
    city_found = cities['_find'](cities, state)  # cities['_find'](cities, state) == find_city(cities, state)
    print(city_found)
