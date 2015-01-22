// Does this string have unique char?

#include <iostream>
using namespace std;

// ASCII maps to 128 characters
const int CHAR_SET_SIZE = 128;

bool string_has_unique_char(string input_string){
	bool map[CHAR_SET_SIZE - 1]; 
	for(int i = 0; i < input_string.length(); i++){
		if (map[int(input_string[i])])
			return false;
		
		map[int(input_string[i])] = true;
	}
	return true;
}

int main() {
	string s1 = "abcdefghij";
	string s2 = "abcee329";
	string s3 = "2921skj2";

	cout << string_has_unique_char(s1) << endl;
	cout << string_has_unique_char(s2) << endl;
	cout << string_has_unique_char(s3) << endl;
	return 0;
}	
