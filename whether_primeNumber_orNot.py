# Algorithm 5: Check whether a number is prime or not

#pseudocode:
"""
Step 1: Start
Step 2: Declare variables n, i, flag.
Step 3: Initialize variables
        flag ← 1
        i ← 2  
Step 4: Read n from the user.
Step 5: Repeat the steps until i=(n/2)
     5.1 If remainder of n÷i equals 0
            flag ← 0
            Go to step 6
     5.2 i ← i+1
Step 6: If flag = 0
           Display n is not prime
        else
           Display n is prime
Step 7: Stop 
"""

# Step 1: Start
# Step 2: Declare variables n, i, flag.
# Step 3: Initialize variables
#         flag ← 1
#         i ← 2

flag = 1
i = 2

# Step 4: Read n from the user.
n = int(input("Enter a number: "))

# Step 5: Repeat the steps until i=(n/2)
while i <= (n // 2):
    # 5.1 If remainder of n÷i equals 0
    if n % i == 0:
        flag = 0
        break
    # 5.2 i ← i+1
    i += 1

# Step 6: If flag = 0
#            Display n is not prime
#         else
#            Display n is prime
if flag == 0:
    print(f"{n} is not a prime number.")
else:
    print(f"{n} is a prime number.")

# Step 7: Stop

