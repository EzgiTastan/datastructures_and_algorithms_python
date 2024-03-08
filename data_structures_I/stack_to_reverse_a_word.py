# Approach:
# The idea is to create an empty stack and
# one by one push all the characters from the string into it.
# Then pop each character one by one from the stack and
# put them back into the input string starting from the 0’th index.
# As we all know, stacks work on the principle of first in, last out.
# After popping all the elements and placing them back to string, the formed string would be reversed.
# Let's gooo!


# Define a function to create an empty stack.
def createStack():
	stack = []
	return stack

def size(stack):
	return len(stack)

# If the length of the stack is 0 (if the stack is empty), return True.
def isEmpty(stack):
	if size(stack) == 0:
		return True

#Define a new function called "push" to add elements one by one. (It increases the size by 1)
def push(stack, item):
	stack.append(item)

#Define another function called "pop" to remove elements one by one from the stack. (Yes, the size decreases by 1)
def pop(stack):
	if isEmpty(stack):
		return
	return stack.pop()

#It will continues till the whole stack is empty. Therefore;
#We write "if isEmpty(stack)"
# else, it will continue popping the items!

#Alright, those parts also exist in the "stack_py" document, so let's reverse the string now!
# A stack based function to reverse a string


#Define a brand-new function called as "reverse". It will take the user input.
# The user input will be equal to string variable.
#reverse function will take string as its argument.
#Also, the length of the string -provided by user- will be equal to n.
def reverse(string):
	n = len(string)

	# Create an empty stack. Instead of just calling the function,
    #We have assign its value to a new variable 'stack'
	stack = createStack()

	# Push all characters of string to stack by using for loop!
    # a note: range is used as   range(start, stop, step)
    #So it will start from 0 till n by incrementing 1!
    #push is used like this       push(the stack name, what you want to add)
	for i in range(0, n, 1):
		push(stack, string[i])

	# This step can be seen as a preparation to create a reversed string.
    #Empty the whole string. Because the reversed version of it will be again assigned to this variable!
	string = ""

	# Pop all characters of string (just like we pushed all the characters) and put them back to string
    # for i in range(0, n, 1) starts with the 0 till (n-1)(the last element's index) and it will increment 1 in each step
    # This for loop is used to add the removed characters.
    # string += pop(stack) removes one element after each loop. And adds it to the string
    # Since it adds what had been removed beforehand, the string is reversed!
	for i in range(0, n, 1):
		string += pop(stack)

	return string


# Driver program to test above functions
string = "TheStackTopicIsTheEasiestOneThanksToEzgiTastan"
string = reverse(string)
print("Reversed string is " + string)

