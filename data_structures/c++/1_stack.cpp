#include <cstdlib>
#include <iostream>

using namespace std;

int MAX_STACK_SIZE = 500;


class Stack{
private:
   int top;
   int items[MAX_STACK_SIZE] = {};

public:
    Stack();
    void push(int data);
    void is_empty();
    int pop(int data);
    // int peek();
    // int size();
}; 

Stack::Stack(){
    top = -1;
}

void Stack::push(int data){
    top += 1;
    items[top] = data;
}

int Stack::pop(int data){
    if (top ==  -1){
        return 0;
    }
}

int main(int argc, char** argv){
    Stack Test;

    Test.push(7);
    Test.push(8);
    Test.push(9);

    cout << Test.items;
}