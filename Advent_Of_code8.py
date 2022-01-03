from typing import List

unique_lens: List[int]= [2,3,4,7] 
input_ : List[str] = []
with open(r'D:\Coding\Python\handy\cases.txt','r') as f:
    while True:
        line :str = f.readline()
        if not line:
            break
        input_.append(line.replace("\n",""))
        
#print([w for w in [word for word in [words.split(" ") for words in [puzzle.split('|')[0]  for puzzle in [x for x in input_]]]] ])
#print(len([1 for w in sum([word.split(" ")for word in[puzzle.split("|")[1] for puzzle in input_]],[]) if len(w) in unique_lens]))
values : List[int] = []
for single_patern , output_value in [puzzle.split("|") for puzzle in input_]:
    numbers : List[str] = ["" for _ in range(10)]
    all_numbers :str  = sorted(single_patern.split(" ")[:-1],key = lambda x : len(x))
    numbers[1] = all_numbers.pop(0)
    numbers[7] = all_numbers.pop(0)
    numbers[4] = all_numbers.pop(0)
    numbers[8] = all_numbers.pop(6)
    numbers[9] = [x for x in all_numbers[3:] if len([y for y in numbers[4] if y not in x ]) == 0][0]
    numbers[6] = [x for x in all_numbers[3:] if len([y for y in numbers[1] if y not in x ]) == 1][0]
    numbers[0] = [x for x in all_numbers[3:] if x not in [numbers[9],numbers[6]]][0]
    numbers[3] = [x for x in all_numbers[:3] if len([y for y in numbers[1] if y not in x ]) == 0][0]
    numbers[5] = [x for x in all_numbers[:3] if len([y for y in numbers[6] if y not in x ]) == 1][0]
    numbers[2] = [x for x in all_numbers[:3] if x not in [numbers[3],numbers[5]]][0]
    values.append((int("".join(map(str,[numbers.index(n) for n in sum([list(filter(lambda x: sorted(x) == sorted(number),numbers))for number in output_value.split(" ")],[])])))))
print(sum(values))    
    
    
    