# First, store our temperature readings in variables.

temp1 = 27.3
temp2 = 25.9
temp3 = 28
temp4 = 26.5

# Next, apply the formula for the average of a set:
#
#   avg = (sum of everything) / (number of things)
#
# Keep in mind that we need a _variable_ to keep store the sum of temperatures.

temp_sum = 0

# Now, add the values of each temperature reading into the temp_sum variable
# Recall that the `=` sign does not mean mathematically equal. It is just a
# shortform notation for assignment.

temp_sum = temp_sum + temp1
temp_sum = temp_sum + temp2
temp_sum = temp_sum + temp3
temp_sum = temp_sum + temp4

# Finally, apply the formula for the average.

temp_sample_size = 4
temp_avg = temp_sum / temp_sample_size

# And get python to show it to us by _printing_ it onto the screen.

print(temp_avg)
