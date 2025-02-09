# Demonstrate the usage of Counter objects

from collections import Counter


# list of students in class 1
class1 = ["Bob", "James", "Chad", "Darcy", "Penny", "Hannah",
          "Kevin", "James", "Melanie", "Becky", "Steve", "Frank"]

# list of students in class 2
class2 = ["Bill", "Barry", "Cindy", "Debbie", "Frank",
          "Gabby", "Kelly", "James", "Joe", "Sam", "Tara", "Ziggy"]

# TODO: Create a Counter for class1 and class2
c1 = Counter(class1)
c2 = Counter(class2)
print(c1)
print(c2)

# TODO: How many students in class 1 named James?
print(f'students named James in Class1: {c1["James"]}')

# TODO: How many students are in class 1?
print(f'total students in Class1: {sum(c1.values())}')

# TODO: Combine the two classes
c1.update(class2)
print(c1)
print(f'total students in Class1: {sum(c1.values())}')

# TODO: What's the most common name in the two classes?
print(f'most common name in two classes combined: {c1.most_common(3)}')

# TODO: Separate the classes again
c1.subtract(class2)
print(f'separated Class2 from c1 counter again: {c1}')

# TODO: What's common between the two classes?
print(f'common names between two classes: {c1 & c2}')

# TODO: counter for number of chars in string 'mississippi'
print(f'frequence of characters in mississippi: {Counter("mississippi")}')

# check https://realpython.com/python-counter/
