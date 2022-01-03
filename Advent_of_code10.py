from typing import List,Dict


opposites = {'{':'}','[':']','(':')','<':'>'}
sytnax_error_reword = {')':1,']':2,'}':3,'>':4}
in_put = [r"[({(<(())[]>[[{[]{<()<>>",
        r"[(()[<>])]({[<{<<[]>>(",
        r"{([(<{}[<>[]}>{[]{[(<()>",
        r"(((({<>}<{<{<>}{[]{[]{}",
        r"[[<[([]))<([[{}[[()]]]",
        r"[{[{({}]{}}([{[{{{}}([]",
        r"{<[[]]>}<{[{[{[]{()[[[]",
        r"[<(<(<(<{}))><([]([]()",
        r"<{([([[(<>()){}]>(<<{{",
        r"<{([{{}}[<[[[<>{}]]]>[]]",]
points = []

def get_data(path):
    with open(path, 'r') as f:
        in_ = []
        for line in f.readlines():
            in_.append(line.replace(" ","")[:-1])
    return in_
in_put= get_data(r'D:\Coding\Python\handy\cases.txt')

for line in in_put:
    queue : List[str] = []
    for symbol in line:
        if symbol not in opposites.keys() and symbol != queue[-1]:
            break
        elif symbol in opposites.keys():
            queue.append(opposites[symbol])
        else:
            queue.pop()
    else:
        if len(queue) != 0:
            temp_points = 0
            for i in reversed(queue):
                temp_points *= 5
                temp_points += sytnax_error_reword[i]
            points.append(temp_points)

print(sorted(points)[(len(points)-1)//2])
