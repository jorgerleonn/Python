#CHALLENGUE 1
mi_lista = [1,1,2]

def append_size(my_list):
    my_list.append(len(my_list))
    return my_list

#CHALLENGUE 2
def append_sum(my_list):
    i = 1
    sum = []
    while i < 4:
        sum = my_list[-2] + my_list[-1]
        my_list.append(sum)
        i += 1
    return my_list
        
#CHALLENGUE 3
def larger_list(my_list1,my_list2):
    if len(my_list1) >= len(my_list2):
        return my_list1[-1]
    else: return my_list2[-1]
    
#CHALLENGUE 4
def more_than_n(my_list,item,n):
    if my_list.count(item) > n:
        return True
    else: return False
    
#CHALLENGUE 5
def combine_sort(my_list1,my_list2):
    lista = my_list1 + my_list2
    lista.sort()
    return lista
    
#ADVANCED LIST CHALLENGUES
#CHALLENGUE 1
def every_three_nums(start):
    return list(range(start,100,3))

#CHALLENGUE 2
def remove_middle(my_list,start,end):
    return my_list[:start] + my_list[end+1:]
    
#CHALLENGUE 3
def more_frequent_item(my_list,item1,item2):
    if my_list.count(item1) >= my_list.count(item2):
        return item1
    else: return item2
    
#CHALLENGUE 4
def double_index(my_list,index):
        my_list[index] = my_list[index]*2
        return my_list
    
#CHALLENGUE 5
def middle_element(my_list):
    if len(my_list) % 2 == 0:
        return (my_list[int(len(my_list)/2)] + my_list[int(len(my_list)/2 - 1)])/2
    else: return my_list[int(len(my_list)/2)]

print(middle_element([5, 2, -10, -4, 4, 5]))