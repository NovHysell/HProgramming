#map function
numbers = [1, 2, 3, 4]
squared = map(lambda x: x**2, numbers)
print(list(squared))
#use when you need to transform every element in an iterable

words = ['python', 'c', 'java']
loud = map(lambda word: word.title(), words)
print(list(loud))

texts = ['    Hello   World   ', 'Python   Programming', '   Data   Science   ']
cleaned = map(lambda s: ' '.join(s.split()), texts)
print(list(cleaned))

#filter()
#applies a predicate function to each item in an iterable and returns an iterator containing only the items for which the function returns
numbers = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x%2 == 0, numbers)
print(list(even))

numbers = [1, 2, 3, 4, 5, 6]
result = map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers))
print(list(result))

# Comprehensions are concise ways to create lists, dictionaries, or sets by applying an expression to each item in an iterable
# [expression for item in iterable(number)]
squares = [x**2 for x in range(5)]
print(squares)
evens = [x for x in range(10) if x % 2 == 0]
print(evens)