def add_list(list_a, list_b):
    # Write your implementation here
    return list_a+list_b

def sub_list(list_a, list_b):
    # Write your implementation here
    list_c=[]
    for a in list_a:
        if a not in list_b:
            list_c.append(a)
    return list_c


def max_list(list_a):
    # Write your implementation here
    return max(list_a)

def sort_list(list_a):
    # Write your implementation here
    return sorted(list_a)