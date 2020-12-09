# Exercise Title: H5P Dictionaries and Loops
---
# Instructional Requirements
## Key Technical Outcome

## Exercise Context

## Exercise Instructions

Q1: Below is a dictionary containing flight numbers and the IATA codes for the international airports from which they depart.
Drag and drop the proper values into the missing portions of the code block to output the following sentence "Flight [flight number] departs from [airport]:

<pre>
flights = { 124 : 'LAX',  156: 'JFK',  87: 'MIA', 35: 'IAD', 78: 'HNL' }
 
for f in flights:
 	print("Flight " + str(_) + " departs from " + _ ) # <b> f and flights[f] </b>
 </pre>
 
[ options for drag and drop:  f, f[flightd], flights, flights[f]] 
  
Q2: We would like to modify our output to print the names of the airports instead of their IATA codes. We have added an additional dictionary whose keys are IATA codes and values are airport names. 

<pre>
flights = { 124 : 'LAX',  156: 'JFK',  87: 'MIA', 35: 'IAD', 78: 'HNL' }
airport_names = { 'LAX': 'Los Angeles', 'JFK': 'John F Kennedy', 'MIA': 'Miami', 'IAD': 'Washington Dulles', 'HNL': 'Daniel K. Inouye'}

for f in flights:
	 IATA = _______ # <b> flights[f] </b>
 	print("Flight " + str( _ ) + " departs from " + ____)  #  <b>f and airport_names[IATA]</b>
</pre>
 	
[options for drag and drop : flights[f], airport_names[IATA], airport_names[f], f]

Q3: What is the value of d after the for loop:

<pre>
d = { 'a': 1, 'b': 2, 'c': 3, 'd': 4}

for key in dictionary:
 d[key] = d[key]*2
</pre>

a. d = {'a': 1, 'b': 2, 'c': 3, 'd': 4} <br>
b. d = {'a': 2, 'b': 4, 'c': 6, 'd': 8} # <b>correct </b> <br>
c. d = {'aa': 1, 'bb': 2, 'cc': 3, 'dd': 4} <br>

Q4: Using the dictionary below, answer whether the following questions will return True or False.

<pre>cars = {'Camry': 'Toyota', 'Malibu': 'Chevrolet', 'Mustang': 'Ford', 'M-Class': 'Mercedes-Benz'}</pre>

'Camry' in cars.values() F <br>
'Chevrolet' in cars.keys() F <br>
'Ford' in cars.values() T <br>
