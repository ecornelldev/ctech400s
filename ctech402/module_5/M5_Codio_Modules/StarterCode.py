import stats

my_list = [4,1,5,7,6,8,9,10,8,3,3,8,12]

my_mean  = stats.mean(my_list)
print('The mean is: ' +  str(my_mean))

my_median = stats.median(my_list)
print('The median is: ' +  str(my_median))

my_range = stats.range(my_list)
print('The range is: ' +  str(my_range))

my_std_dev = stats.standard_deviation(my_list)
print('The standard deviation is: ' + str(my_std_dev))
