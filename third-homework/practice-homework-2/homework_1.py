def merge_lists(first_list, second_list):
    return first_list + second_list


def get_first_value(t):
    return t[0]


def sort_list(list_tuples):
    list_tuples.sort(key=get_first_value)
    return list_tuples


list1 = [(1, "apple"), (3, "orange"), (5, "banana")]
list2 = [(2, "grape"), (4, "kiwi"), (6, "melon")]

merged_tuples = merge_lists(list1, list2)
print(merged_tuples)
print(sort_list(merged_tuples))
