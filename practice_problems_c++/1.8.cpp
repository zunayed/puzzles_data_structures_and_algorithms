#include<iostream>

using namespace std;

bool is_rotation(string s1, string s2) {
    
    if(s1.length() == s2.length() && s1 != ""){
        string s1s1 = s1 + s1;
        size_t found = s1s1.find(s2);
        if (found != string::npos){
            return true;
        }
    }
    
    return false;
}

int main() {
    string s1 = "waterbottle";
    string s2 = "erbottlewat";

    cout <<  is_rotation(s1, s2);
}
