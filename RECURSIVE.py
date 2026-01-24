def recursive_list_sum(data_list):
    total = 0
    for element in data_list:
        if type (element)==list:
            total = total+recursive_list_sum(elements)
        else:
            total = total + element
    return total
print(recursive_list_sum([1,2,[3,4],[5,6]]))


