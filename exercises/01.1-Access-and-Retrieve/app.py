
my_list = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']

# 1. print the item here
print(my_list[2])

# 2. change the position were 'thursday' is to None
position = my_list.index("thursday")
my_list[position]= None


# 3. print that position now here
print(my_list[position])