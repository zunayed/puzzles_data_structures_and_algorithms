//  

#include <iostream>
#include <assert.h>

using namespace std;

void replace_space(char *input, int size) {
    int num_of_spaces = 0;
    int new_size;

    for(int i = 0; i < size; i++) { 
        if(input[i] == ' ') {
            num_of_spaces++;
        }
    }    

    new_size = size + num_of_spaces * 2;
    input[new_size] = '\0';

    for(int i = size - 1; i > 0; i--) {
        if (input[i] == ' ') {
            input[new_size - 1] = '0';
            input[new_size - 2] = '2';
            input[new_size - 3] = '%';

            new_size = new_size - 3; 
        } else {
            input[new_size - 1] = input[i];
            new_size = new_size - 1;
        }
    } 
}

int main() {

    char test[50] = "Mr John  Smith ";
    replace_space(test, strlen(test));
    cout << test; 
    return 0;
 }	
