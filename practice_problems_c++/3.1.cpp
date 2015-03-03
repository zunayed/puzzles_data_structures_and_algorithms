// Implment a stack with one array 
#include <iostream>


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
            std::fill_n(array, array_size, NULL);
            std::fill_n(pointer, num_stacks, -1);
        }

        ~SingleArrayStacks (){
            delete[] array;
            delete[] pointer;
        }

        void print_stack(int stack_num){
            std::cout << "Current stack state: ";
            for (int i = 0; i < sizeof(array); i++) {
                std::cout << array[i];
            }
            std::cout << std::endl;
        }

        void push (int stack_num, int val){
            if (pointer[stack_num] > stack_size) {
                std::cout << "Stack Full \n"; 
            } else {
                std::cout << "Pushing: " << val;
                array[get_top_position(stack_num) + 1] = val;
                pointer[stack_num]++;
            }
            print_stack(stack_num);
        }

        int pop(int stack_num){
            if (pointer[stack_num] == -1) {
                return NULL;
            } else {
                std::cout << "Poping from stack: " << stack_num << std::endl;
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
    std::cout << "Poping vals \n";
    std::cout << array.pop(0) << std::endl;  
    std::cout << array.pop(0) << std::endl; 

    array.push(0, 1);
    array.push(0, 2);
    array.push(2, 4);
    array.push(2, 6);

    std::cout << array.pop(2) << std::endl;
    std::cout << array.pop(0) << std::endl; 
    std::cout << array.pop(2) << std::endl;
    std::cout << array.pop(2) << std::endl;
    
}
