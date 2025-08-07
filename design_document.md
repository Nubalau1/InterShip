# Design Document – Anagram Finder

## Approach and Reasoning

The program uses the frequency of each letter in a word to generate a unique key. Words that share the same key are grouped together using a hash map.

### Why Letter Frequency Instead of Sorted Strings?

Instead of sorting the characters of each word (which is common in similar problems), I chose to use a 26-element frequency list (one index per letter from 'a' to 'z'). This is converted to a tuple to be used as a dictionary key.

- **Time Complexity:** Frequency counting is `O(n)`, whereas sorting is `O(n log n)`.
- **Space Complexity:** The 26-length array is constant size, regardless of word length.
- **Performance:** Better for large datasets with longer words or millions of entries.

### Maintainability
Modular Structure: Although implemented in a single script, the logic can easily be separated into functions (e.g., read_input(), group_anagrams(), write_output()).

No Dependencies: Uses only Python’s standard library, reducing external issues and keeping setup simple.

### Scalability
**For ~10 Million Words**
- The current implementation reads all words into memory.
- This is acceptable on modern machines, as 10 million average-length words (~60MB) fit easily in RAM.

**For ~100 Billion Words**
- The current implementation is not sufficient since 100 billion average-length words is ~477GB.

**Solution for Very Large Files**

To handle extremely large files, we can process the file line by line or in chunks. Also, we can store the result in a database so that it doesn't use all the memory of the RAM.
