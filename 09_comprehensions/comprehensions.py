# Comprehensions are concise ways to create lists, dictionaries, or sets by applying an expression to each item in an iterable
# [expression for item in iterable(number)]
squares = [x**2 for x in range(5)]
print(squares)
evens = [x for x in range(10) if x % 2 == 0]
print(evens)

# Create a function that resturns squares of even numbers in the given range
def squares_of_evens(start, end):
    return [x**2 for x in range(start, end) if x % 2 == 0]

print(squares_of_evens(4, 19))
print(squares_of_evens(10, 100))

def long_upper_words(words):
    """Return a list of uppercase words longer than 3 characters"""
    return [word.upper() for word in words if len(word) > 3]

words = ["hello", "banana", "BMW", "bye"]
print(long_upper_words(words))

# Create a function that returns a dictionary mapping each word to its length from a list of words
def word_lengths(words):
    """return {key:value} #TODO
    for word in words:
        key = word
        value = len(word)"""
    print("WIP")

print(word_lengths(words))