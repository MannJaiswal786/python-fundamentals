num_set = {1,2,3,4, (5,6)}
print(num_set)

words_set = {"Alpha", "Bravo", "Charlie"}
abcd = ""
for word in words_set:
    abcd += word

print(abcd)

words_set.add("Mann")
words_set.discard("Alpha")

print(words_set)