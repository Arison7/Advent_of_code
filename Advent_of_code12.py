from typing import List, Dict , Tuple


class graph():
    def __init__(self) -> None:
        
        self.adjencies_list : Dict[int,List[int]] = {}
        self.indexes : List[str] = ["start","end"]
        self.paths = []
        
    def inicialize_adjencies_list(self, data : List[str]) -> None:
        for from_,to_ in [line.split("-") for line in data]:
            if from_ not in self.indexes:
                self.indexes.append(from_)
            if to_ not in self.indexes:
                self.indexes.append(to_)
            from_index = self.indexes.index(from_)
            to_index = self.indexes.index(to_)
            if from_index not in self.adjencies_list.keys():
                self.adjencies_list[from_index] = [to_index]
            else:
                self.adjencies_list[from_index].append(to_index)
            if to_index not in self.adjencies_list.keys() :
                self.adjencies_list[to_index] = [from_index]
            else:
                self.adjencies_list[to_index].append(from_index)
        self.indexes[0] = self.indexes[0].upper()
        self.indexes[1] = self.indexes[1].upper()

    def dfs(self,path = [],visted = [],limit = 1,current = 0) -> None:
        path.append(current)
        if current ==1:
            self.paths.append(path)
            return
        for neiboard in self.adjencies_list[current]:
            if neiboard != 0:
                if self.indexes[neiboard].isupper():
                    self.dfs(path.copy(),visted.copy(),limit,neiboard)
                elif neiboard not in visted:
                    self.dfs(path.copy(),visted.copy() + [neiboard],limit,neiboard)
                elif neiboard in visted and limit != 0:
                    self.dfs(path.copy(),visted.copy() + [neiboard],limit -1,neiboard)
                    
    
    def get_data(self,path) -> None:
        data = []
        with open(path, 'r') as f:
            for line in f.readlines():
                data.append(line.replace('\n',''))
        self.inicialize_adjencies_list(data)

                
            
    

def main():
    g = graph()
    g.get_data(r"D:\Coding\Python\handy\cases.txt")
    
    g.dfs()
    print(len(g.paths))
    """ for x in g.paths:
        print(list(map(lambda x :g.indexes[x],x))) """
if __name__ == "__main__":
    main()
    
