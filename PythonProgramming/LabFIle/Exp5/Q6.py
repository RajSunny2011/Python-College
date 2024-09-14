# 6.	Program to count number of unique words in a given sentence using sets.
sentence = "I am Satvik Raj studing in UPES"
words = sentence.split()
unique_words = set(words)
print("Number of unique words:", len(unique_words))
