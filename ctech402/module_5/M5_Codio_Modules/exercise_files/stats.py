# A module of statistical functions.

# Calculate the mean of a list of numbers.
def mean(numbers):
    return sum(numbers) / float(len(numbers))

# Calculate the median of a list of numbers.
def median(numbers):
    # First, sort the numbers.
    sorted_numbers = sorted(numbers)

    # If we have an odd length list, pick the middle one.
    if len(numbers) % 2 == 0:
        return sorted_numbers[len(numbers) // 2]

    # If we have an even length list, average the middle two.
    else:
        middle1 = sorted_numbers[len(numbers) // 2]
        middle2 = sorted_numbers[len(numbers) // 2 - 1]
        return (middle1 + middle2) / 2.0

# Calculate the range (biggest minus smallest).
def range(numbers):
    return max(numbers) - min(numbers)

# Calculate the standard_deviation of the list of numbers
def standard_deviation(numbers):
	# complete function
	 
	
	#return standard deviation
	return 
