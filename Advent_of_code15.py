from typing import List, Dict, Tuple
import heapq

#$ A*
class A_star():
    def __init__(self) -> int:
        self.parents = {}
        self.gScore ={}
        self.pQueue = Priority_queue((0,0))
        self.goal = ()
        self.grid = []
    
    def calculate(self) -> int:
        while len(self.pQueue.heap) > 0:
            current = self.pQueue.de_queue()
            if current == self.goal:
                return self.gScore[self.goal]
            #options = [(0,1),(0,-1),(1,0),(-1,0),(-1,1),(-1,-1),(1,1),(1,-1)]
            options = [(0,1),(0,-1),(1,0),(-1,0)]
            for option in options:
                neiboard = (current[0] + option[0],current[1] + option[1])
                if 0 <= neiboard[0] < len(self.grid) and 0 <= neiboard[1] < len(self.grid[0]):
                    current_score = self.gScore[current] + self.grid[neiboard[0]][neiboard[1]]
                    if current_score < self.gScore[neiboard]:
                        self.parents[neiboard] = current
                        self.gScore[neiboard] = current_score
                        self.pQueue.queue_in(current_score,neiboard)
        return -1
    def get_data(self,path) -> None:
        with open(path,'r') as f:
            while True:
                line : str = f.readline()
                if not line:
                    break
                self.grid.append(list(map(int,line.replace('\n',''))))
    def set_up(self)-> None:        
        self.goal = (len(self.grid)-1,len(self.grid[0])-1)
        for i in range(self.goal[0]+1):
            for j in range(self.goal[1]+1):
                self.parents.setdefault((i,j),None)
                self.gScore.setdefault((i,j),1e400)
        self.gScore[(0,0)] = 0
    def expand_map(self) -> None:
        new_map = [l.copy() for l in self.grid]
        len_grid = len(self.grid)
        len_grid_row = len(self.grid[0])
        while len(new_map) < len_grid*5 or len(new_map[len(new_map)-1]) < len_grid_row*5:
            self.increment()
            
            for i in range(len(new_map)):
                if len(new_map[i]) < len_grid_row*5:
                    new_map[i].extend(self.grid[(i%len_grid)].copy())  
            if len(new_map) < len_grid *5:
                new_map.extend([l.copy() for l in self.grid])
        self.grid = new_map
        self.set_up()
    def increment(self) -> None:
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                self.grid[i][j] += (1 - (9*(self.grid[i][j]//9)))
                
            
        
        
    
        
                           
class Priority_queue():
    def __init__(self,start_point):
        self.heap = []
        self.start_point = start_point
        self.queue_in(0,start_point)
    
    #? retruns euclidean distance between two points
    @classmethod
    def euclidean_distance(self=None,point_a : Tuple[int] = (0,0),point_b : Tuple[int] = (0,0)) -> float:
        return ((point_b[0] - point_a[0])**2+((point_b[1] - point_a[1])**2))**1/2 
    
    def queue_in(self,distance : int,position) -> None:
        heapq.heappush(self.heap,(self.euclidean_distance(self.start_point,position)+distance,position))
        
    def de_queue(self) -> Tuple[int,int]:
        return heapq.heappop(self.heap)[1]
        
    
def reconstruct(path,end,star):
    
    path.append(end)
    current = star.parents[end]
    if current == None:
        return
    reconstruct(path,current,star)



def main():
    star = A_star()
    star.get_data(r'') # path for your puzzle input
    star.expand_map()
    print(star.calculate())
    
    
    
    

    
    
if __name__ == '__main__':
    main()