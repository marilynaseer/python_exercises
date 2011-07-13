#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

class StringReverser
{
	public:
		string reverse(string string_to_reverse)
		{	
			int len = string_to_reverse.length();
			string reversed_string = "";
			for( int i = 0; i < len; i++) 
			{
				char c = string_to_reverse[len-(i+1)];
				reversed_string = reversed_string + c;
			}
			
			return reversed_string;
		}
};

int main()
{
	StringReverser reverser;
	string reversed_string = reverser.reverse("test");
	cout << reversed_string << endl;
	return 0;
}
