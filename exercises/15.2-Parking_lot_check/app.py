parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

#Your code go here:
def get_parking_lot(parking_state):
    new_parking=[]
    state={}
    total_slots=0
    available_slots=0
    occupied_slots=0
    for each in parking_state:
        for each2 in each:
            if each2!=0:
                total_slots+=1
            if each2==2:
                available_slots+=1
            elif each2==1:
                occupied_slots+=1
    state['total_slots']=total_slots
    state['available_slots']=available_slots
    state['occupied_slots']=occupied_slots
    return state
print(get_parking_lot(parking_state))


