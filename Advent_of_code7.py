from typing import List, Tuple


class Crabby_marines:
    def __init__(self) -> None:
        self.crabs : List[int]  = []
        
    def calculate_fuel_cost(self,number:int):
     
        return sum([sum(range(abs(x-number)+1)) for x in self.crabs])
    
    def finding_balance(self,number:int,balancer:int,pre_cost :int ) -> int:
        next_ = self.calculate_fuel_cost(number + balancer)
        if pre_cost <= next_:
            return pre_cost
        return self.finding_balance(number + balancer,balancer,next_)
        
        
    def allinge(self) -> int:
        start  = sum(self.crabs)//len(self.crabs)
        base_fuel_used :int = self.calculate_fuel_cost(start)
        base_fuel_up :int = self.calculate_fuel_cost(start+1)
        base_fuel_down :int = self.calculate_fuel_cost(start-1)
        target :int = min(base_fuel_down,base_fuel_used,base_fuel_up)
        if base_fuel_used == target:
            return base_fuel_used
        elif base_fuel_up == target:
            return self.finding_balance(start+1,1,base_fuel_up)
        else:
            return self.finding_balance(start-1,-1,base_fuel_down)
    def get_data(self,path : str):
        temp = ""
        with open(path , 'r') as f:
            for line in f.readlines():
                temp += line
        self.crabs = list(map(int,temp.split(',')))
    
            
        
     
crab = Crabby_marines()
crab.get_data(r"D:\Coding\Python\handy\cases.txt")
print(crab.allinge())
    
    



