#include <cstdlib>
#include <iostream>

using namespace std;

int MAX_STACK_SIZE = 500;


class Stack{
private:
   int top;
   items = new int[MAX_STACK_SIZE];
public:
    Stack();
    void push();
    void is_empty();
    int pop();
    int peek();
    int size();
}

Stack::Stack(){
    top = -1;
}