#QUESTION 3
#Here is a function that determines if a number is palindrome or not:
def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

# Which of the below is NOT a palindrome?
print(palindrome("5485839837501070045005400701057389385845"))

print(palindrome("7489617719749244646336564429479177169847"))

print(palindrome("8025833559061079503003059701609553385208"))

print(palindrome("6593036601359343374664733439531066303956"))