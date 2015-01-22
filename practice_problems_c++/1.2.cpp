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
	string s1 = "abcdefghij";
	string s2 = "abcee329";
	string s3 = "2921skj2";

	return 0;
}	
