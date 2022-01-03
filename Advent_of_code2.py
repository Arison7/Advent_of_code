from os import path
from typing import List, Tuple 

puzzle : List[int]  = []
def get_data(path:str):
    with open(path, 'r') as f:
        for line in f.readlines():
            puzzle.append(tuple(line.replace("\n","").split(" ")))
 

#puzzle = [("forward",5),("dowm",5),("forward",8),("up",3),("down",8),("forward",2)]

def Dive(puzzle:Tuple[str,str]) -> int:
    aim : int = 0
    deapth : int = 0
    horizontal : int = 0
    for p in puzzle:
        if p[0] == "down":
            aim += int(p[1])
        elif p[0] == "up":
            aim -= int(p[1])
        else:
            horizontal += int(p[1])
            deapth += aim * int(p[1])
    return horizontal*deapth

get_data(r'D:\Coding\Python\handy\cases.txt')
print(Dive(puzzle))