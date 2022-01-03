from typing import List,Dict,Tuple
import time


#starts timer
start = time.time_ns()

#loads data from file
def get_data() -> Tuple[List[list],List[int]]:
    with open(r'D:\Coding\Python\handy\cases.txt','r') as f:
        in_puts : List[int] = list(map(int, (f.readline()).replace('\n','').split(",")))
        puzzles = []
        preperation = []
        while True:
            current : str = f.readline()
            if current == '':
                puzzles.append(preperation.copy())
                preperation.clear()
                break
            if current == '\n':
                puzzles.append(preperation.copy())
                preperation.clear()
                
                continue
            
            preperation.append(list(map(int,current.replace('\n','').replace("  "," ").split(" "))))     
            
                
    return puzzles[1:], in_puts
#puzzle being list of all boards where
#*board -> list of list of ints
#in_puts being list of ints      
puzzle, in_puts = get_data()

class Number:
    #*The list of all Number object with represeting them real numbers 
    Numbers = {}
    #*List of index of boards that have already won
    winners:int = []
    
    #$index of all 3 list are 
    #
    #
    #
    #
    def __init__(self,index: Tuple[int,int], board: List[List[int]],original:int) -> None:
        self.indexs : List[Tuple[int,int]] = [index]
        self.boards : List[List[List[int]]] = [board]
        self.original_index : List[int] = [original]
        self.present : bool = False

    def add(self, index: Tuple[int,int], board: List[List[int]],original:int) -> None:
        self.boards.append(board)
        self.indexs.append(index)
        self.original_index.append(original)
    def idk(self) -> None:
        for j in range(len(self.boards)):
            result : Tuple [int,bool] = self.victory_check(j)
            if(result[1]):
                self.winners.append(self.original_index[result[0]])
            #return caculation(Number.Numbers[i].boards[result[0]],i)
    
    def victory_check(self,i:int) -> Tuple[int,bool]:
        if(self.check_line(i)) and (self.original_index[i] not in self.winners):
            return [i,True]
        return [0,False]

    def check_line(self,i :int) -> bool:   

        index: Tuple[int,int] = self.indexs[i]
        board: List[List[int]] = self.boards[i]
        
        for y in range(len(board)):
            if not self.Numbers[board[y][index[0]]].present:
                break
        else:
            return True
        for x in range(len(board[index[1]])):
            if not self.Numbers[board[index[1]][x]].present:
                break
        else:
            return True
        return False
            
def calculation(board, h : int) -> int:
    result : int = 0
    for i in board:
        for j in i:
            if not (Number.Numbers[j].present):
                result += j
    return result*h

def inicialize_dictionary(board : List[List[int]],original:int) -> None: 
    for y,row in enumerate(board):
        for x,number in enumerate(row):
            if number in Number.Numbers.keys():
                Number.Numbers[number].add((x,y),board,original)
            else : 
                Number.Numbers[number] = Number((x,y),board,original)
                
for i,board in enumerate(puzzle):
    inicialize_dictionary(board,i)
    
def operation_start(in_puts:List[int])->int:            
    for i in in_puts:           
        if i in Number.Numbers.keys() :
            Number.Numbers[i].present = True
            Number.Numbers[i].idk()
        if len(Number.winners) == len(puzzle):
            Number.Numbers[i].present = True
            return calculation(puzzle[Number.winners[-1]],i)  
            
            
print(operation_start(in_puts))
end = time.time_ns()
print((end - start) /1000000 , " ms")     
                

    
    
        

