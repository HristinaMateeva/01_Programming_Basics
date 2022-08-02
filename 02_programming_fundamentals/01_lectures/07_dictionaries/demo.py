# my_dict = {'orange': 'portokal', 'apple': 'qbylka'}
# my_dict['orange'] = "something else"
# print(my_dict.get('orange'))
#
# my_list = [1, 2, 3]
# my_list[0] = 100
# print(my_list)


# my_dict = {'Peter': 21, 'George': 18, 'John': 45}
# sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[0], reverse=True))
#
# print(sorted_dict)

# Nested dictionaries
words = {'a': {1: "first"}, 'b': {2: "second"}}
for word, nums in words.items():
    for key, value in nums.items():
        print(key)