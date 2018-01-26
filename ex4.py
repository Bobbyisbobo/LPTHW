cars = 100 #定义汽车的数量
space_in_a_car = 4  #定义每辆车的载客量
drivers = 30  #定义司机的数量
passengers = 90  #定义乘客的数量
cars_not_driven = cars - drivers #计算没有被开车辆的数量
cars_driven = drivers  #定义已被开车辆的数量
carpool_capacity = cars_driven * space_in_a_car #计算载客量
average_passengers_per_car = passengers / cars_driven  #计算平均每辆汽车的载客辆


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport",carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", int(average_passengers_per_car), "in each car.")
