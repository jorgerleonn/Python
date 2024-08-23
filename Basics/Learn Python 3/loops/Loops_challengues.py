#CHALLENGUE 1
def divisible_by_ten(nums):
    count = 0
    for numbers in nums:
        if numbers % 2 == 0:
            count += 1
    return count
#print(divisible_by_ten([1,3,5,2,10,20]))
      
        
#CHALLENGUE 2
def add_greetings(names):
    names_list = []
    for name in names:
        names_list.append("Hello, " + name)
    return names_list
    
#print(add_greetings(["Owen", "Max", "Sophie"]))

#CHALLENGUE 3 
def delete_starting_evens(lst):
    while (len(lst) > 0 and lst[0] %2 == 0): #Si el número que se encuentra es par, entra a la condición
       lst = lst[1:] #ahora cambia la lista por otra nueva, quitando su primer elemento 0
    return lst #devuelve la lista cuando termine el bucle

#print(delete_starting_evens([4, 8, 10, 11, 12, 15]))

#CHALLENGUE 4
def odd_indices(lst):
    new_list = []
    for i in range(1,len(lst),2):#el 2 es porque va incrementando de 2 en 2
        new_list.append(lst[i])
    return new_list

#print(odd_indices([4, 3, 7, 10, 11, -2]))

#CHALLENGUE 5
def exponents(bases,powers):
    new_list = []
    for i in bases:
        for power in powers:
            new_list.append(i**power)
    return new_list

#print(exponents([2, 3, 4], [1, 2, 3]))


#CHALLENGUE 1
def sum(lst):
    sum = 0
    i = 0
    while i < len(lst):
        sum = sum + lst[i]
        i += 1
    return sum
        
def larger_sum(lst1,lst2):
    if sum(lst1) >= sum(lst2):
        return lst1
    else: return lst2
#print(larger_sum([1, 9, 5], [2, 3, 7]))

#CHALLENGUE 2
def over_nine_thousand(lst):
    sum = 0
    i = 0
    while i < len(lst):
        sum = sum + lst[i]
        if sum > 9000:
            return sum
        i += 1
    return sum

#CHALLENGUE 3
def max_num(nums):
    return max(nums)

#CHALLENGUE 4
def same_values(lst1, lst2):
  new_lst = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      new_lst.append(index)
  return new_lst

#print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
            
        
#CHALLENGUE 5
def reversed_list(lst1,lst2):
    if lst1 == list(reversed(lst2)):
        return True
    else: return False
            
print(reversed_list([1, 2, 3], [3, 2, 1]))
    