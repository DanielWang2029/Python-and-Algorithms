

print(2 * 3)  # multiplication
print(2 ** 3)  # power operation
zeros_and_ones = [0, 1] * 10  # create a list with 10 zeros and ones ([0, 1, 0, 1 ... 0, 1])
string = "AB" * 10  # create a string with 10 "AB"s


def foo(*args, **kwargs):  # define args and kwargs
    pass


my_list = [1, 2, 3]
my_dict = {'a': 1, 'b': 2, 'c': 3}
foo(*my_list, **my_dict)  # unpacking arguments to function parameters

numbers = (1, 2, 3, 4, 5, 6, 7)
*beginning, last = numbers  # unpack multiple remaining elements of a list/tuple/set, always unpacked to a list
print(beginning, last)  # print [1, 2, 3, 4, 5, 6] and 7

begin, *middle, secondlast, last = numbers
print(begin, middle, secondlast, last)  # print 1, [2, 3, 4, 5], 6, 7
print()

my_tuple = (11, 22, 33)
my_set = {444, 555, 666}
new_list = [*my_tuple, *my_list, *my_set]  # unpack list/tuple/set when merging a new list
print(new_list)  # print [11, 22, 33, 1, 2, 3, 666, 555, 444]  where elements of the set not necessarily in that order

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4, 'e': 5, 'f': 6}
dict_merge = {**dict1, **dict2}
print(dict_merge)  # print the union of dict1 and dict2
