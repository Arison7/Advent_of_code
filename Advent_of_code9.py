from typing import List,Tuple
from math import prod

#matrix2 =  [list(map(int,z)) for z in [(lambda x: [y for y in str(x)])(x) for x in matrix]]
def get_data(path :str ) ->  List[List[int]]:
    out_matrix : List[List[int]] = []
    with open(path) as f:
        for line in f.readlines():
            temp_list : List[int] = []
            for ch in line:
                if ch == '\n':
                    break
                temp_list.append(int(ch))
            out_matrix.append(temp_list)
    return out_matrix      
matrix = get_data(r'D:\Coding\Python\handy\cases.txt')  
def martix_traversal(x:int = 0,y:int = 0,size:List[int] = 0) -> None:
    position :int = matrix[y][x]
    options : List[Tuple[int,int]] = [(0,1),(0,-1),(1,0),(-1,0)] 
    not_deep = True
    for option in options:
        new_x = x + option[0]
        new_y = y + option[1]
        if 0 <= new_x < len(matrix[0]) and 0 <= new_y < len(matrix) and (new_x,new_y) not in visited and matrix[new_y][new_x] < position:
            martix_traversal(new_x,new_y,size)
            not_deep = False
    if not_deep:
        size[0] += 1
        out_spread(x,y,size)
def out_spread(x,y,size):
    visited.append((x,y))
    position :int = matrix[y][x]
    options : List[Tuple[int,int]] = [(0,1),(0,-1),(1,0),(-1,0)] 
    for option in options:
        new_x = x + option[0]
        new_y = y + option[1]
        if 0 <= new_x < len(matrix[0]) and 0 <= new_y < len(matrix) and (new_x,new_y) not in visited and matrix[new_y][new_x] > position and matrix[new_y][new_x] != 9 :
            size[0] += 1
            out_spread(new_x,new_y,size)
               
    
visited = []
out_put = []
for y in range(len(matrix)):
    for x in range(len(matrix[0])):
        if (x,y) not in visited and matrix[y][x] != 9:
            number = [0]
            martix_traversal(x,y,number)
            out_put.append(number[0]) 
print(prod(sorted(out_put,reverse=True)[:3]))


    
