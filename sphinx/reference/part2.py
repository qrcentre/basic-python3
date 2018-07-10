from basic_python3 import *

# First, let's get a _list_ of current temperature readings across singapore.

temp_list = weather_get_now()

# Just like in part 1, we need a variable to store the sum of temperatures.

temp_sum = 0

# In order to sum everything up, we need to visit the temperatures in the list
# of temperatures _one by one_---that is, we must iterate through it.

for x in temp_list:
    temp_sum = temp_sum + x

# Now, we find the number of things with the special _method_ `len`.

temp_sample_size = len(temp_list)
temp_avg = temp_sum / temp_sample_size

print(temp_avg)

# Is it hot or is it cold?.

if temp_avg > 27:
    print("It's pretty warm tonight")
else:
    print("naise")
