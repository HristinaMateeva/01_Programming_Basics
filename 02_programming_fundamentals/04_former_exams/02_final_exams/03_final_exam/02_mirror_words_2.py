import re

text = input()
pattern = r"(@|#)(?P<word_1>[a-zA-Z]{3,})\1{2}(?P<word_2>[a-zA-Z]{3,})\1"

mirror_words = {}
mirror_pair = ""
result = []

match_words = re.finditer(pattern, text)
pairs_list = [obj.group() for obj in re.finditer(pattern, text)]

if pairs_list:
    print(f"{len(pairs_list)} word pairs found!")
    for match in match_words:
        pairs_dict = match.groupdict()
        word_one = pairs_dict['word_1']
        word_two = pairs_dict['word_2']
        if word_one == word_two[::-1]:
            mirror_words[word_one] = word_two
    if mirror_words:
        print("The mirror words are:")
        for first_word, second_word in mirror_words.items():
            mirror_pair = f"{first_word} <=> {second_word}"
            result.append(mirror_pair)
        print(', '.join(result))
    else:
        print("No mirror words!")
else:
    print("No word pairs found!")
    print("No mirror words!")
