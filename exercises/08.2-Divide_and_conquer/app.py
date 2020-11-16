list_of_numbers = [4,	80,	85,	59,	37,25,	5,	64,	66,	81,20,	64,	41,	22,	76,76,	55,	96,	2,	68]


#Your code here:
def merge_two_list(list_of_numbers):
    odd=[]
    even=[]
    new_list=[]
    for i in range(0,len(list_of_numbers)):
        if list_of_numbers[i]%2!=0:
            odd.append(list_of_numbers[i])
        else:
            even.append(list_of_numbers[i])
    new_list.append(odd)
    new_list.append(even)
    return new_list

print(merge_two_list(list_of_numbers))

