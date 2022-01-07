from typing import List,Dict
from itertools import tee,chain,zip_longest
from collections import Counter

def pairwise(iterable):
    a,b = tee(iterable)
    next(b,None)
    return zip(a,b)

class Extended_Polymerization():
    def __init__(self,steps):
        
        self.polymer_template = {}
        self.polymer = Counter()
        self.counter = Counter()
        
        self.steps = steps
    def expantions(self,steps) -> Dict[str,int]:
        if steps == 0:
            return self.polymer
        self.polymer = self.expantions(steps-1)
        temp_counter = Counter()
        for pair in self.polymer.items():
            new = self.polymer_template[pair[0]]
            self.counter[new] += pair[1]
            temp_counter[pair[0][0] +new] += pair[1]
            temp_counter[new+pair[0][1] ] += pair[1]
        self.polymer = temp_counter
        
        return self.polymer
    def get_data(self,path) -> None:
        with open(path, 'r') as f:
            in_put :str = list(f.readline().replace('\n',''))
            self.polymer = Counter([_[0]+_[1] for _ in pairwise(in_put)])
            self.counter = Counter(in_put)
            f.readline()
            for line in f.readlines():
                
                temp = line.replace("\n","").replace(" ",'').split('->')
                
                self.polymer_template[temp[0]] = temp[1]
    def calculate(self):
        self.expantions(self.steps)
        
        commons = self.counter.most_common()
        
        return commons[0][1] - commons[len(commons)-1][1]

def main():
    ext = Extended_Polymerization(40)
    ext.get_data(r'D:\Coding\Python\handy\cases.txt')
    
    print(ext.calculate())
    


if __name__ == '__main__':
    main()

