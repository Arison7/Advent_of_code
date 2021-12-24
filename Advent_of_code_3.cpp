#include <iostream>

//TODO:Get a max size of a bin represatation of a number
#define TEMP 4
int Binary_diagnostic(int puzzle[]){
    int count[TEMP]{0};
    for(int i;i < sizeof(puzzle)/sizeof(int);i++){
        if(puzzle[i]&1<<i)
            count[i]++;
        else
            count[i]--;
    }
    int gamma = 0;
    for(int i;i < TEMP;i++){
        if (count[i])
            gamma&1<<i;
        
    }
    
    return gamma*(~gamma);
    
}


int main(){
    int p[] = {0b00100,0b11110,0b10110,0b10111,0b10101,0b01111,0b00111,0b11100,0b10000,0b11001,0b00010,0b01010};
    std::cout<< Binary_diagnostic(p);
}