from typing import Dict,List,Tuple 


#*Types alliases 
Line = Tuple[Tuple[int,int],Tuple[int,int]]
#*variables
points : Dict[Tuple[int,int],int]= {}
lines = []

def get_data(path):
    with open(path , "r") as f:
        for line in f.readlines():
            if not line:
                break
            temp = [x for x in line.replace("\n", "").replace(" ","").split("->")]
            lines.append((tuple(map(int,temp[0].split(","))),tuple(map(int,temp[1].split(",")))))
def changable_func(symbol : str,n:int) : 
    func = f'''
def temp_func(line):
    for i in range(line[0][{n}],line[1][{n}]{symbol}1,{symbol}1):
        new =  i
        if {f"(new,line[0][{1-n}])" if n == 0 else f"(line[0][{1-n}],new)" } in points.keys():
            points[{f"(new,line[0][{1-n}])" if n == 0 else f"(line[0][{1-n}],new)" }] += 1
        else: 
            points[{f"(new,line[0][{1-n}])" if n == 0 else f"(line[0][{1-n}],new)" }] = 1
    '''
    exec(func ,globals())
    return temp_func
   
def rec_traversal(curr,go_to) -> None:
    if curr in points.keys():
        points[curr] += 1
    else:
        points[curr] = 1
    if curr == go_to:
        return
    rec_traversal((curr[0] - 1 if curr[0] > go_to[0] else curr[0] + 1,curr[1] - 1 if curr[1] > go_to[1] else curr[1] + 1),go_to)
        
    
    
def insert_lines(lines: List[Line]) -> None:
    for line in lines:
        if line[0][0] != line[1][0] and line[0][1] != line[1][1]:
            rec_traversal(line[0],line[1])
            continue
        if line[0][0] != line[1][0]:
            f =  changable_func("-" if line[0][0] > line[1][0] else "+", 0)
            f(line)
        elif line[0][1] != line[1][1]:
            f =  changable_func("-" if line[0][1] > line[1][1] else "+", 1)
            f(line)
        else:
            if line[0] in points.keys():
                points[line[0]] += 1
            else: 
                points[line[0]] = 1
    
        
get_data(r"D:\Coding\Python\handy\cases.txt") 
insert_lines(lines)

out = len([value for _,value in points.items() if value > 1])

print(out)