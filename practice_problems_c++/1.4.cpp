//  

#include <iostream>
#include <assert.h>

using namespace std;

void replace_space(char *input, int size) {
    int num_of_spaces = 0;
    int new_size;

    for(int i = 0; i < size; i++) { 
        if(input[i] == " ") {
            num_of_spaces++;
        }
    }    

    new_size = size + num_of_spaces * 2;
    cout << input;
    input[new_size] = '\0';
    cout << input;

    for(int i = size - 1; i > 0; i--) {
        if (input[i] == " ") {
            input[new_size - 1] = "0";
            input[new_size - 2] = "2";
            input[new_size - 3] = "3";

            new_size = new_size - 3; 
        } else {
            input[new_size - 1] = input[i];
            new_size = new_size - 1;
        }
    } 
}

int main() {

    char[] s = "hello ?";
    replace_space(s);
    assert(s = "hello%20?");
    cout << s; 
    return 0;
 }	
