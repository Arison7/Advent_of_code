from typing import List ,Tuple




class squids:
    def __init__(self,steps : int) -> None:
        self.grid = [list(map(int,z)) for z in [(lambda x:
            [y for y in str(x)])(x) for x in ["7147713556",
                                               "6167733555",
                                               "5183482118",
                                               "3885424521",
                                               "7533644611",
                                               "3877764863",
                                               "7636874333",
                                               "8687188533",
                                               "7467115265",
                                               "1626573134",]]]  

        
        self.lighted : List[Tuple] = []
        self.flashes :int  = 0
        self.steps: int = steps
    def increment(self) -> None:
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                self.grid[i][j] += 1   
                if self.grid[i][j] > 9:
                    self.lighted.append((i,j))
                    self.flashes += 1  
                
    def step_through(self)-> int:
        while True:
            self.flashes = 0 
            self.lighted.clear()
            self.increment()
            for elighted in self.lighted:
                self.spread(elighted)
            for elighted in self.lighted:
                self.grid[elighted[0]][elighted[1]] = 0
            self.steps +=1
            if self.flashes == (len(self.grid)*len(self.grid[0])):
                return self.steps
        
            
    def spread(self,position) -> None:
        options = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]
        for option in options:
            new_y = position[0]
            new_x = position[1]
            new_y += option[0]
            new_x += option[1]
            if 0 <= new_y< len(self.grid) and 0 <= new_x < len(self.grid[0]) and (new_y,new_x) not in self.lighted:
                self.grid[new_y][new_x] += 1
                if self.grid[new_y][new_x] > 9:
                    self.lighted.append((new_y,new_x))
                    self.flashes += 1
                    
                    

def main():
    squid_field = squids(0)
    print(squid_field.step_through())
                  
if __name__ == '__main__':
    main()            