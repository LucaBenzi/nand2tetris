#include <iostream>
#include <list>
#include <string.h>
#include<stdlib.h>

using namespace std;

class Constant{
	string name;
	int value;
	
public:
	
	Constant(){
		name = "";
	}
	
	Constant(string s, int v){
		name = s;
		value = v;
	}
	
	string getname() {
		return name;
	}
	
	int getvalue() {
		return value;
	}
};

//********should be in constant.h*************
void predefinedConstant(list<Constant> &constList);
bool find (list<Constant> &constList , string n);
int getValue(list<Constant> &constList , string n);
//*******should be in file_operations.h*****
void removeSpace(char *str);
void removeComment(char *str);
//*******should be in assembler.h************
bool hasMoreCommands(char *str , FILE* fp);
int commandType(char * str);
//*******should be in general_functions.h or in main file
bool isNumber(char* s);







int main()
{
FILE *fsource, *fout;
int i;
char str[200];
list<Constant> constList;
list<Constant>::iterator p;
int lineNumber = 0;

	predefinedConstant(constList);
	
	fsource = fopen("Mult.asm","r");
	fout = fopen("1.temp","w");
	
// -> remove blank space, blank line and comments
	while(hasMoreCommands(str,fsource))
	{
		if(str[0] != '\n')	//remove empty line
		{
			removeComment(str);
			removeSpace(str);
			fputs(str,fout);
		}
	}
	fclose(fsource);
	fclose(fout);
	
	fsource = fopen("1.temp","r");
	fout = fopen("2.temp","w");
	
// -> insert new constant and remove type 3 instruction
	while(hasMoreCommands(str,fsource))
	{
		lineNumber++;
		
		if(commandType(str) == 3)
		{
		char s[100];
			
			for(i = 0; str[i+1] != ')';i++)
			{
				s[i] = str[i+1];
			}
			s[i] = '\0';
			constList.push_back(Constant(s,lineNumber));
			
		}
		else
			fputs(str,fout);
	}
	
	fclose(fsource);
	fclose(fout);
	
	fsource = fopen("2.temp","r");
	fout = fopen("3.temp","w");
	while(hasMoreCommands(str,fsource))
	{
		
		if(commandType(str) == 1)		//use switch case
		{
		int num;
		char *p;
		char binNum[16];
		string s;
		char t[16];
			
			p = &str[1];
			s = str;
			if(!isNumber(p))
			{
			list<Constant>::iterator it;
	
				for(it = constList.begin(); it != constList.end(); it++)
				{
					if(s.compare(1,s.size()-2,it->getname()) == 0)				//remember that s has a '\n' before '\0'
					{
						//transform it->getvalue into binary number and write it into 3.temp
						sprintf(t,""
						
					}
				}
					
			}
			else
			{
				num = atoi(p);
			}
			sprintf(binNum,"@%d\n",num); 
			//fputs(binNum,fout);
		}
		else
		{
			//fputs(str,fout);
		}
	}
	
	//remove("copy.asm");	//remove the file
	getchar();
	return 0;
}









bool isNumber(char* s)
{
	if((*s >='0') && (*s <= '9'))
		return true;
	else
		return false;
}

//****************************************************should be in file_operations.cpp**********************************************
void removeSpace(char *str)		//remove all the space in a string
{
int lenght, i, j, k;

	lenght = strlen(str);
	
	for(i = 0; i < lenght; i++)
	{
		if(str[i] == ' ')
		{
			//shift del resto del vettore
			lenght--;
			for(j = i; j < lenght+1; j++)
			{
				k = j + 1;
				str[j] = str[k];
			}
			i--;	
		}

	}
}

void removeComment(char *str)		//replace the first '/' with '\0' chapter
{
int i, lenght;
	
	lenght = strlen(str);
	
	for(i = 0; i < lenght-1; i++)
		if((str[i] == '/') && (str[i+1] == '/'))
			str[i] = '\0';
	
}

//****************************************************should be in constant.cpp****************************************************
void predefinedConstant(list<Constant> &constList)
{
	//register
	constList.push_back(Constant("R0",0));
	constList.push_back(Constant("R1",1));
	constList.push_back(Constant("R2",2));
	constList.push_back(Constant("R3",3));
	constList.push_back(Constant("R4",4));
	constList.push_back(Constant("R5",5));
	constList.push_back(Constant("R6",6));
	constList.push_back(Constant("R7",7));
	constList.push_back(Constant("R8",8));
	constList.push_back(Constant("R9",9));
	constList.push_back(Constant("R10",10));
	constList.push_back(Constant("R11",11));
	constList.push_back(Constant("R12",12));
	constList.push_back(Constant("R13",13));
	constList.push_back(Constant("R14",14));
	constList.push_back(Constant("R15",15));
	//other constants
	constList.push_back(Constant("SP",0));
	constList.push_back(Constant("LCL",1));
	constList.push_back(Constant("ARG",2));
	constList.push_back(Constant("THIS",3));
	constList.push_back(Constant("THAT",4));
	constList.push_back(Constant("SCREEN",16384));
	constList.push_back(Constant("KBD",24567));
	
}

bool find (list<Constant> &constList , string n)
{
	list<Constant>::iterator p;
	
	for(p = constList.begin(); p != constList.end(); p++)
		if(p->getname().compare(n))
			cout << "ciao";	
		
		//if(n.compare(p->getname())==0)
		//{
		//	printf("%s",p->getname());
		//	return true;
		//}
			
	
	return false;
}

int getValue(list<Constant> &constList , string n)
{
	list<Constant>::iterator p;
	
	for(p = constList.begin(); p != constList.end(); p++)
		if(n.compare(p->getname())==0)
			return p->getvalue();
	
	return false;
}

//*******************************************************should be in assembler.cpp*************************************************
bool hasMoreCommands(char *str , FILE* fp)
{
	if(fgets(str,200,fp))
		return true;
	else
		return false;
}

int commandType(char * str)
{
	if(str[0] == '@')
		return 1;
	else if(str[0] == '(')
		return 3;
	else if(str[0] == 'A' || str[0] == 'D' || str[0] == 'M')
		return 2;
	else
		return 0; //error condition
}



