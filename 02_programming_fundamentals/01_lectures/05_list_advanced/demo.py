def convert_to_int(el):
    return int(el)

nums_as_string = ["1", "2", "3"]
# numbers = [int(el) for el in nums_as_string]  #Първи вариант
# numbers = [convert_to_int(el) for el in nums_as_string]  #Втори вариант
# numbers = list(map(int, nums_as_string))  #Трети вариант
numbers = list(map(lambda el: int(el), nums_as_string))  #Четвърти вариант
