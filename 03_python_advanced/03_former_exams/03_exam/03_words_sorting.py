def words_sorting(*args):
    words_dict = {}
    sum_words = 0
    result = ""
    for word in args:
        words_dict[word] = 0
        for char in word:
            words_dict[word] += ord(char)
        sum_words += words_dict[word]
    if sum_words % 2 == 1:
        sorted_dict = dict(sorted(words_dict.items(), key=lambda x: -x[1]))
    else:
        sorted_dict = dict(sorted(words_dict.items(), key=lambda x: x[0]))
    for key, value in sorted_dict.items():
        result += f"{key} - {value}\n"
    return result


# ------------------------------
print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))
# ------------------------------
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))
# ------------------------------
print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
