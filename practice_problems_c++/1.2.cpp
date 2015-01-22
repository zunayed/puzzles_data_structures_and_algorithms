// void function reverse(char* str) 
// do it in place and be wary of null pointer

#include <iostream>
using namespace std;

void reverse(char* str) {
	char* end = str;
	char temp;

	if(str){
		//get pointer to the end of string
		while(*end){
			end++;
		}		
		end--; // back one to avoid null pointer
		while(str < end) {
			temp = *str;
			*str++ = *end;
			*end-- = temp;
		}	
	}
}

int main() {
    char s[] = "1234567890";
    reverse(s);
    cout << s;
    return 0;
}	
