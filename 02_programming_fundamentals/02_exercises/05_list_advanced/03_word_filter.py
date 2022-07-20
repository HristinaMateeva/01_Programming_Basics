words = input().split()
filtered_words = [word for word in words if len(word) % 2 == 0]
print("\n".join(filtered_words)) #can be written like that: print(*filtered_words, sep="\n")
