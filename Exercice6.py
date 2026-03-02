# QUESTION 6
# Here is some code:

import random

random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# We go through the list using the indexes (so we can modify the list values)
for i in range(len(random_numbers)):

    # If the number is odd -> replace it by its negative (ex: 7 becomes -7)
    if random_numbers[i] % 2 == 1:
        random_numbers[i] = -random_numbers[i]

    # Else it is even -> replace it by its double (ex: 8 becomes 16)
    else:
        random_numbers[i] = random_numbers[i] * 2

# Print the final modified list
print(random_numbers)
# continue here
#Continue by removing the odd numbers from the list and replace them with their negative counterparts (1 is replaced by -1).
# Also replace the even numbers with their double value
# print the list at the end
# Use only what we have learned in class. Provide some explanation in the form of comments.