// Implment a stack with one array 
#include <iostream>
using namespace std;


class SingleArrayStacks{
    private:
        int stack_size;
        int *array;
        int *pointer;
        int get_top_position(int stack_num){
            return (stack_num * stack_num)  + pointer[stack_num]; 
        }

    public:
        SingleArrayStacks (int array_size = 100, int num_stacks = 3) {
            array = new int[array_size];    
            pointer = new int[num_stacks]; 
            stack_size =  array_size / num_stacks;
            fill_n(array, array_size, NULL);
            fill_n(pointer, num_stacks, -1);
        }

        ~SingleArrayStacks (){
            delete[] array;
            delete[] pointer;
        }

        void print_stack(int stack_num){
            cout << "Current stack state: ";
            for (int i = 0; i < sizeof(array); i++) {
                cout << array[i];
            }
            cout << endl;
        }

        void push (int stack_num, int val){
            if (pointer[stack_num] > stack_size) {
                std:cout << "Stack Full \n"; 
            } else {
                cout << "Pushing: " << val;
                array[get_top_position(stack_num) + 1] = val;
                pointer[stack_num]++;
            }
            print_stack(stack_num);
        }

        int pop(int stack_num){
            if (pointer[stack_num] == -1) {
                return NULL;
            } else {
                cout << "Poping from stack: " << stack_num << endl;
                print_stack(stack_num);
                int val = array[get_top_position(stack_num)];
                array[get_top_position(stack_num)] = NULL;
                pointer[stack_num]--;

                return val;
            }
        }
};

int main() {
    SingleArrayStacks array(91, 3); 
    array.push(0, 7);
    array.push(0, 4);
    cout << "Poping vals \n";
    cout << array.pop(0) << endl;   // 2 
    cout << array.pop(0) << endl;   // 1

    array.push(0, 1);
    array.push(0, 2);
    array.push(2, 4);
    array.push(2, 6);

    cout << array.pop(2) << endl;   // 6
    cout << array.pop(0) << endl;   // 2
    cout << array.pop(2) << endl;   // 4
    cout << array.pop(2) << endl;   // 0
    
}
