


class parsing:
    packages = []
    def __init__(self,binary_representation:str) -> None:
        self.success = False
        if len(binary_representation) < 11:
            return 
        self.version = int(binary_representation[:3],2)
        self.id_ = int(binary_representation[3:6],2)
        self.binary_representation = binary_representation[6:]
        self.literial_value = ""
        self.length_id = None
        self.special_number = 0
        self.success = True
        parsing.packages.append(self)
       
    def initialize_literal(self,i,j):
        group = self.binary_representation[i:j]
        self.literial_value += group[1:]
        if group[0] == '0':
            return j + 6
        return self.initialize_literal(i+5,j+5) 
        
    def initialize_operator(self):
        if self.binary_representation[0] == '0':
            return self.size_mode()
        else: 
            return self.amount_mode()
            
    def size_mode(self):
        self.special_number = int(self.binary_representation[1:16],2)
        new_sub_packet = parsing(self.binary_representation[16:16+self.special_number])
        break_point = new_sub_packet.calculate()
        while 16+self.special_number -(16+break_point) > 6:
            new_sub_packet = parsing(self.binary_representation[16+break_point:16+self.special_number])
            if not new_sub_packet.success:
                break
            break_point += new_sub_packet.calculate()
        return self.special_number + 22
    
    def amount_mode(self):
        self.special_number = int(self.binary_representation[1:12],2)
        new_sub_packet = parsing(self.binary_representation[12:])
        break_point = new_sub_packet.calculate()

        self.special_number -= 1
        while self.special_number != 0:
            new_sub_packet = parsing(self.binary_representation[12+break_point:])
            if not new_sub_packet.success:
                break
            break_point += new_sub_packet.calculate()
            self.special_number -= 1
        return break_point + 18
    

    def calculate(self):
        if self.id_ == 4:
            return self.initialize_literal(0,5)
        else:
            return self.initialize_operator()
    
        
        
        
def get_data(path):
    data = ''
    with open(path, 'r') as f:
        for line in f.readlines():
            data += line.replace('\n', '')
    return data
            
           

        


def casting_binary(hex_:str) -> str:
    binary = ""
    for hex_number in hex_:
        number_without_leading_zeros = str((bin(int(hex_number,16)))).replace("0b","")
        number_without_leading_zeros = "0"*(4-len(number_without_leading_zeros)) + number_without_leading_zeros 
        binary += number_without_leading_zeros
    return binary

    


def main():
    data : str = get_data(r'')
    first = parsing(casting_binary(data))
    first.calculate()
    print(sum([p.version for p in first.packages]))
    
  
    
    



if __name__ == "__main__":
    main()