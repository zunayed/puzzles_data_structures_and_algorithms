/*
Implement a method to perform basic string compression
using the counts of repeated characters. For example,
the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the
 original string, your method should return the original string.
*/

#include <iostream>
#include <assert.h>


using namespace std;

string compress_string(string s1) {
   
    int char_count = 0;
    string new_string = "";    

    for(int i = 0; i < s1.length(); i ++) {
        if(s1[i] == s1[i+1]) {
            char_count += 1;
       
        } else {
            char_count = 1;
            new_string += s1[i] + to_string(char_count);
        }
     }

    if(s1.length() < new_string.length())
        return s1;
        
    return new_string;
}

int main() {
    string s1  = "aabcccccaaa";
    string new_string = compress_string(s1);
    cout << new_string; 
}
