from typing import List 
from math import ceil

class paper:
    def __init__(self) -> None:
        #*              x, y    
        self.points = [(6,10),(1,14),(9,10),(1,3),(10,4),(4,11),(6,0),(6,12),(4,1),(0,13),(10,12),(3,4),(3,0),(8,4),(1,10),(2,14),(8,10),(9,0),]
        #*y = 1 and x = 0
        self.instructions = [(0,5),(0,5)]
    def fold(self):
        instraction =  self.instructions.pop(0)
        if instraction[0] == 1:
            self.points.sort(key = lambda x: x[1])
            print(self.points)
            print(self.find_lower(instraction[1],1,len(self.points)//2))
        else:
            self.points.sort(key = lambda x: x[0])
            print(self.points)
            print(self.find_lower(instraction[1],0,len(self.points)//2))
    def find_lower(self,number,index,j,i=0)->int:
        if i == j or j == len(self.points) -1:
            return j
        if self.points[j][index] <= number and self.points[j+1][index] > number:
            return j +1 
        if self.points[j][index] <= number:
            return self.find_lower(number,index,j+j//2 if j +j//2 < len(self.points) else len(self.points)-1,j)
        else: 
            return self.find_lower(number,index,j-ceil((j-i)/2),i)
            
        
        
def main():
    p = paper()
    p.fold()
    




if __name__ == '__main__':
    main()