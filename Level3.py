s = input("enter words: ")

words = s.split()

total_words = len(words)

stats = {}
for word in words:
    stats[word] = stats.get(word, 0) + 1

print(f"\ntotal count of words: {total_words}")
print("unique words stats:")

for word, count in stats.items():
    print(f"{word}: {count}")
