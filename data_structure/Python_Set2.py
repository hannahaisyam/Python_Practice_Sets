#1 Create a Python Set such that it shows element from both list in pair

def exercise1():
    first_list = [2,3,4,5,6,7,8]
    second_list = [4,9,16,25,36,49,64]

    result = zip(first_list, second_list)
    result_set = set(result)
    print(result_set)

#2 Find the intersection (common) of two sets and remove those elements from first set

def exercise2(set1,set2):
    new_sets = []
 #we can use isdisjoint method, but in this case we're not using
    for elem in set1:
        if elem in set2:
            new_sets.append(elem)
    
    print(new_sets)
    
set1 = [23,42,65,56,78,83,29]
set2 = [57,93,29,67,73,43,23]
#exercise2(set1, set2)

#3 Remove duplicate from a list and create tuple and find the min and max num

list = [56, 23, 11, 56, 73, 56]
unique_list = []


unique_list = set(list)

def getMax(number):
    max = number[0]
    for value in range(1,len(number)):
       if number[value] > max:
           max = number[value]
    return max 

def getMin(number):
    min = number[0]
    for value in range(1,len(number)):
       if min > number[value]:
           min = number[value]
    return min



print(f"unique items = {unique_list}")
print(f"this is tuple = {tuple(unique_list)}")
print(f"max : {getMax(list)}")
print(f"min : {getMin(list)}")