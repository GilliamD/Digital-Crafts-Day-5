"""Write a letter_histogram program that asks the user for input,
and prints a dictionary containing the tally of how many times
each letter in the alphabet was used in the word. For example:

$ python letter_histogram.py
Please enter a word: banana
{'a': 3, 'b': 1, 'n': 2}"""

text = "bannana"
x = 0
bucket = {}

while x < len(text):
    x += 1
    print(text)
