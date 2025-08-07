from collections import defaultdict

one_word_list = []

# Reading and storing the words in a list
with open(file="../sample.txt", mode="r") as input_file:
    for word in input_file:
        one_word_list.append(word.strip())

# Grouping words by letter frequency as key
hashmap = defaultdict(list)
for word in one_word_list:
    list_of_indexes = [0] * 26
    for letter in word:
        list_of_indexes[ord(letter) - ord("a")] += 1
    hashmap[tuple(list_of_indexes)].append(word)

# Writing the grouped anagrams to a file
with open(file="../output.txt", mode="w") as output_file:
    for list_of_words in hashmap.values():
        output_file.write(" ".join(list_of_words) + "\n")
