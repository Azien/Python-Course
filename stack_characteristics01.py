#Define the stack
stack = [-2,-8]

#Largest value
def largest(stack):
	big = None
	for large in stack:
		if big is None or large > big:
			big = large
	return big
	
#Smallest value
def smallest(stack):
	tiny = None
	for small in stack:
		if tiny is None or small < tiny:
			tiny = small
	return tiny
	
#Sum up the stack
def summarize(stack):
	sumup = None
	for plus in stack:
		if sumup == None:
			sumup = plus
		else:
			sumup = sumup + plus
	return sumup

#Number of arguments
def countArg(stack):
	count = 0
	for added in stack:
		count = count+1
	return count
	
#Create bigFunction(stack)
def bigFunction(stack):
	print "  Largest value:",largest(stack)
	print " Smallest value:",smallest(stack)
	print "    Total value:",summarize(stack)
	print " Argument count:",countArg(stack)
	
#Print the results
bigFunction(stack)

#Define new stack
print "\nNew stack added"
stack = [21,32,40,2,5,6,8.5,98.8,13,30]
bigFunction(stack)

#Define string stack
print "\nNew stack added"
stack = "dupa"
bigFunction(stack)

#Define string stack no. 2
print "\nNew stack added"
stack = ["haha","hoho","hihi"]
bigFunction(stack)

#Define mixed stack
print "\nNew stack added"
stack = [21,32,40,2,5,6,8.5,-2,-8,98.8,13,30,1,1.8,34.9]
bigFunction(stack)

#Define void stack
print "\nNew stack added"
stack = []
bigFunction(stack)

#Entering new stack
print
stack=raw_input("Please enter new stack: ")
print "\nUser defined stack added"
bigFunction(stack)
