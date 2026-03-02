# Question 8
# Write a function that takes a text filename as parameter. It searches for the longest word that starts with "c" and returns it.
# Use only the things we have learned in class. Give some explanations besides the code.

def longest_c_word(filename):
    # We start with an empty "best" word
    longest_word = ""

    # Open the file and read it line by line (class way)
    with open(filename, "r") as f:
        for line in f:
            # Remove the "\n" at the end, make everything lowercase
            line = line.strip().lower()

            # Split the line into words
            words = line.split()

            # Check each word
            for word in words:
                # Keep only words that start with "c"
                if len(word) > 0 and word[0] == "c":
                    # If this word is longer than what we had, update
                    if len(word) > len(longest_word):
                        longest_word = word

    return longest_word