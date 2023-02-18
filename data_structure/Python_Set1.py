#1 Create a list by picking odd-index from first line and even index items 
#from the second

#Odd index
def odd_method():
    for i in range(len(list1)):
        if i %  2 != 0:
            odd_index.append(list1[i])

    print(f"The odd index numbers is {odd_index}")    


#Even index
def even_method():

    for i in range(len(list2)):
        if i % 2 == 0:
            even_index.append(list2[i])

    print(f"The even index numbers is {even_index}")

list1 = [3,6,9,12,15,18,21]
list2 = [4,8,12,16,20,24,28]
odd_index = []
even_index = []

#odd_method()
#even_method()

#2 Remove and add item in a list 

def exercise2():
    value = list1.pop(4)
    print(f"List after removing element at index 4 {list1}")
    list1.insert(2, value)
    print(f"List after adding element at index 2 {list1}")
    list1.append(value)
    print(f"List after removing element at index 4 {list1}")


#3 Slice list into 3equal chunks and reverse each chunk 

def exercise3() :
    print("Original list ", sample_list)

    length = len(sample_list)
    chunk_size = int(length / 3)
    start = 0
    end = chunk_size

    # run loop 3 times
    for i in range(3):
        # get indexes
        indexes = slice(start, end)
    
        # get chunk
        list_chunk = sample_list[indexes]
        print("Chunk ", i, list_chunk)
    
        # reverse chunk
        print("After reversing it ", list(reversed(list_chunk)))

        start = end
        end += chunk_size

    


#4 Count the occurence of each element from a list
sample_list = [11, 45, 8, 11, 8, 14, 45, 45, 89]
count_dic = dict()

for item in sample_list:
    if item in count_dic:
        count_dic[item] += 1
    else:
        count_dic[item] = 1

print("Printing count of each item " , count_dic)