// Given two strings, write a method to decide if one is a permutation of the other

#include <iostream>
#include <algorithm>
#include <assert.h>

using namespace std;

bool is_permutation(string s1, string s2) {
    if (s1.length() != s2.length())
        return false;   
 
    string sorted_string1 = s1;
    string sorted_string2 = s2;

    std::sort(sorted_string1.begin(), sorted_string1.end());
    std::sort(sorted_string2.begin(), sorted_string2.end()); 
    
    if (sorted_string1 == sorted_string2)
        return true;

    return false;
}

int main() {
    string s1 = "toad";
    string s2 = "doat";

    assert(is_permutation(s1, s2)==1);
    return 0;
}	
