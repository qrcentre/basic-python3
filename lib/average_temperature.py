#! /usr/bin/env python3

from basic_python3 import *

# First, let's get a _list_ of current temperature readings across singapore

temp_list = weather_get_now()

# Next, apply the formula for the average of a set:
#
# 	avg = (sum of everything) / (number of things)
#
# Keep in mind that we need a _variable_ to keep store the sum of temperatures

temp_sum = 0

# In order to sum everything up, we need to visit the temperatures in the list
# of temperatures _one by one_---that is, we must iterate through it. Recall
# that the `=` sign does not mean mathematically equal. It is just a shortform
# notation for assignment

for x in temp_list:
    temp_sum = temp_sum + x

# Now, we find the number of things with the special _method_ `len`

temp_sample_size = len(temp_list)

# Finally, apply the formula for the average

temp_avg = temp_sum / temp_sample_size

# And get python to show it to us by _printing_ it onto the screen

print(temp_avg)

# Is it hot or is it cold?

if temp_avg > 27:
    print("It's pretty warm tonight")
else:
    print("naise")

# Bonus: make a telegram bot out of it

telegram_key = 'T3L3GR4M_K3Y'
telegram_chat_id = 1234567
telegram_send(telegram_key, telegram_chat_id, 'It is currently '+str(temp_avg))
