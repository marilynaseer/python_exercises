#include<iostream>
#include<string>
#include<iomanip>
using namespace std;

class StringConcatenate
{
	private:
		char str[20];

	public:
		StringConcatenate()
		{
			strcpy(str,"");
		}
		
		StringConcatenate(char* s)
		{
			strcpy(str,s);
		}
		
		StringConcatenate operator+(StringConcatenate ptr1)
		{
			StringConcatenate temppointer ;
			strcpy(temppointer.str , str);
			strcat(temppointer.str , ptr1.str);
			return temppointer;
		}
		
		friend ostream& operator << (ostream &out, StringConcatenate &ptr2);
		friend istream& operator >> (istream &in, StringConcatenate &ptr2);
};

istream& operator>>(istream &in,StringConcatente &ptr2)
{	
	cout<<"enter string"
	in>>ptr2.str;
	return in;
}

ostream& operator<<(ostream &out,StringConcatenate &ptr2)
{
	out << ptr2.str;
	return out;
}

int main()
{
	StringConcatenate s1 ;
	StringConcatenate s2 ;
	cout << "string1:\n" ;
	cin << s1 << "\n";
	cout << "string2:\n";
	cin << s2 << "\n";
	StringConcatenate s3 = s1 + s2;
	cout << "string3\n";
	cout << s3;
	return 0;
}
