
all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

#Your code go here:
def filterName(x):
    return x[0]=="R"
resulting_names=list(filter(filterName,all_names))

print(resulting_names)




