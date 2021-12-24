from typing import List, Tuple

#$ aproach one brute force
class Lanternfishes_bf:
    def __init__(self,days_left) -> None:
        self.fishes : List[int] = []
        self.days_left : int = days_left
    def exponential_growth(self) -> None:
        while self.days_left != 0:
            temp_fishes : List[int] = []
            for fish in self.fishes:
                if fish == 0:
                    temp_fishes.append(8)
                    fish = 7
                fish -=1
                temp_fishes.append(fish)
            self.fishes = temp_fishes.copy()
            temp_fishes.clear()
            self.days_left -=1
    def get_data(self,path) -> None:
        with open(path, 'r') as f:
            content : str= ''
            for line in f.readlines():
                content += line
            for n in list(map(int,content.replace('\n','').split(','))):
                self.fishes.append(n)
#$ aproach two grouping
class Lanternfishes_group(Lanternfishes_bf):
    def __init__(self,days_left) -> None:
        super().__init__(days_left)
        self.groups : List[int] = [0 for _ in range(9)]
    def initialization_of_group(self) -> None:
        for fish in self.fishes:
            self.groups[fish] += 1
    def exponential_growth(self) -> None:
        self.initialization_of_group()
        while self.days_left != 0:
            temp_groups : List[int] = [0 for _ in range(9)]
            temp_groups[6] += self.groups[0]
            temp_groups[8] += self.groups[0]
            for i,fish_group in enumerate(self.groups[1:]):
                temp_groups[i] += fish_group
            self.groups = temp_groups.copy()
            temp_groups.clear()
            self.days_left -= 1
    def get_data(self,path) -> None:
        super().get_data(path)  

def main():
    #day_7_a = Lanternfishes_bf(80)
    #day_7_a.get_data(r'D:\Coding\Python\handy\cases.txt')
    #day_7_a.exponential_growth()
    day_7_b = Lanternfishes_group(256)
    day_7_b.get_data(r'D:\Coding\Python\handy\cases.txt')
    day_7_b.exponential_growth()
    print(sum(day_7_b.groups))




if __name__ == '__main__':
    main()