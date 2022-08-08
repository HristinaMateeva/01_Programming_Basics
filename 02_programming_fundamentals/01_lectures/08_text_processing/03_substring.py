word_to_replace = input()
text = input()

while word_to_replace in text:
    text = text.replace(word_to_replace, "")

print(text)
