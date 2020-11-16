par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

parlower = par.lower()

counts = {}
#your code go here:
for i in range(0,len(parlower)):
    # print(parlower[i])
    if i==0:
        counts[parlower[i]]=1 
        print(parlower[i],i)
    elif parlower[i].isspace()==False:         
        if parlower[i] in counts:
            counts[parlower[i]]+=1
        else:
            counts[parlower[i]]=1 
            print(parlower[i],i)

print(counts)
