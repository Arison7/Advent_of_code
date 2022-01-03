from typing import List

messerments : List[int]  = []
def get_data(path:str):
    with open(path, 'r') as f:
        for line in f.readlines():
            messerments.append(int(line.replace("\n","")))        
def decrease_count(mess:int) -> int:
    return len([i for i in range(len(mess)-1) if mess[i] < mess[i+1] ])
def decrease_count_groups(mess : List[int]) -> int:
    return len([i for i in range(len(mess)-3) if sum(mess[i:i+3]) <  sum(mess[i+1:i+4])])
    
#get_data()    
print(decrease_count_groups(messerments))

#print(decrease_count(messerments))