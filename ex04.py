# cars 
cars  = 100
# the space
space_in_a_car = 4.0
# drivers
drivers = 30
#passengers
passengers = 90
#cars_not_drivern
cars_not_driven = cars - drivers
# cars_driven
cars_driven = drivers
# carpool
carpool_capacity = cars_driven * space_in_a_car


print("There are %d cars avaliable" % cars)
print("There are only %d drivers avaliable." % drivers)
print("There will be %d empty cars today." % cars_not_driven)
print("We can transport %f people today." % carpool_capacity)