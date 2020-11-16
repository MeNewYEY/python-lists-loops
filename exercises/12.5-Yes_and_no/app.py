theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

def searchBools(x):
    if x == 0:
        return "woko"
    else:
        return "wiki"
#Your code go here:
new_list=list(map(searchBools,theBools))
print(new_list)
