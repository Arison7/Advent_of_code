from typing import List 
from math import ceil

class paper:
    def __init__(self) -> None:
        #*              x, y    
        self.points = []
        #*y = 1 and x = 0
        self.instructions = []
    def fold(self):
        instraction =  self.instructions.pop(0)
        #fold by y axis
        if instraction[0] == 1:
            self.points.sort(key = lambda x: x[1])
            
            indent : int =  self.find_lower(instraction[1],1,len(self.points)//2)
            self.points = self.points[:indent]+ [(x[0],x[1] - 2*(x[1] - (instraction[1]))) for x in self.points[indent:]]
            #print(len(set(sorted(self.points,key = lambda x: x[1]))))
        #fold by x axis
        #!red comment  
        else:
            self.points.sort(key = lambda x: x[0])
            indent : int =  self.find_lower(instraction[1],0,len(self.points)//2)
            
            #print(indent)
            self.points = [(x[0]- (instraction[1])-1,x[1]) for x in self.points[indent:]]+ [(abs(x[0]-instraction[1])-1,x[1]) for x in self.points[:indent]]
            
            #print(len(set(sorted(self.points,key = lambda x: x[0]))))
    def find_lower(self,number,index,j,i=0)->int:
        if i == j or j == len(self.points) -1:
            return j
        if self.points[j][index] <= number and self.points[j+1][index] > number:
            return j +1 
        if self.points[j][index] <= number:
            return self.find_lower(number,index,j+j//2 if j +j//2 < len(self.points) else len(self.points)-1,j)
        else: 
            return self.find_lower(number,index,j-ceil((j-i)/2),i)
    def get_data(self,path: str) -> None:
        with open(path, 'r') as f:
            line :str = f.readline()
            while line != "\n":
                self.points.append(tuple(map(int,line.replace("\n","").split(","))))
                line = f.readline()
            while line:
                line = f.readline()
                if line == "":
                    break
                temp = line[10:].split("=")   
                
                self.instructions.append((1 if temp[0].endswith("y") else 0,int(temp[1].replace("\n",""))))
            
        
        
def main():
    p = paper()
    p.get_data(r"D:\Coding\Python\handy\cases.txt")
    for _ in range(len(p.instructions)):
        p.fold()
    p.points = set(p.points)
    x_s , y_s = zip(*p.points)
    border_y = max(y_s)
    border_x = max(x_s)
    matrix = [[" " for _ in range(border_x+1)] for y in range(border_y+1)]
    
    for point in p.points:
        matrix[point[1]][point[0]] = "#"
    with open(r"D:\Coding\Python\handy\new.txt",'w') as f :
        for line in matrix:
            f.write(str(list(reversed(line))).strip().replace('\'',"").replace(',','')+"\n")
    
    
    
    
        
    




if __name__ == '__main__':
    main()