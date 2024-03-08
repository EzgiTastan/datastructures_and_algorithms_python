"""
Push: Add an element to the top of a stack
Pop: Remove an element from the top of a stack
IsEmpty: Check if the stack is empty
IsFull: Check if the stack is full
Peek: Get the value of the top element without removing it
"""

# Stack implementation in python


# Creating a stack
def create_stack():
    stack = []
    return stack


# Creating an empty stack
def check_empty(stack):
    return len(stack) == 0
#If there are not any elements exist in stack (so the length of the stack will be zero),
# It will return False. If it is equal to 0, it will return True.

# Adding items into the stack
def push(stack, item):
    stack.append(item)
    print("pushed item: " + item)
#To add a new element, we use 'append'. stack.append(item)
#And we will print the new value.


# Removing an element from the stack
def pop(stack):
    if (check_empty(stack)):
        return "stack is empty"

    return stack.pop()
# To remove one element from the stack, we use 'pop'.
# first, we define a pop method that takes stack as an argument
# then, we should check whether the stack is empty or not.
# if it is empty, (len(stack) == 0), then return this: "stack is empty"
# if it is not empty, continue popping! (return stack.pop())


stack = create_stack()
#We should create a new, empty stack with "stack = create_stack()"
# We've defined create_stack() like this: "stack = []" and "return stack"

#Now, we are ready to use "push" to add an element to the stack!
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))

#By using "pop", now we can remove items (Last In First Out -LIFO-) from our stack.
print("popped item: " + pop(stack))

#Since the last element which was added was 4, we remove 4 first.
#pop(stack)
#print("The popped item is :" + pop(stack))

#As a last step, it might be user-friendly (well, also beginner-friendly, too) to write this:
#print("The remaining stack is :" + str(stack)) so that we can see the whole stack!
print("stack after popping an element: " + str(stack))
