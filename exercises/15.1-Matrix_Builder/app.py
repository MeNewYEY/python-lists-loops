# Import random
# import random
# List=[]
# List2=[]
#Create the function below:
# def matrixBuilder(number):
#     for i in range(0,number):
#         List2.append(1)
#     for j in range(0,number):
#         List.append(List2)      
#     return List
# print(matrixBuilder(3))

def matrixBuilder(numb):
    new_list =[[1 for i in range(numb)] for x in range (numb)]
    return new_list
print(matrixBuilder(5))
