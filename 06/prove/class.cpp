#include <iostream>
#include <list>
#include <string>
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

void predefinedConstant(list<Constant> &constList);
bool find (list<Constant> &constList , string n);

int main()
{
	list<Constant> constList;
	list<Constant>::iterator p;
	
	
	predefinedConstant(constList);
	for(p = constList.begin(); p != constList.end(); p++) {
		cout<< p->getname() << '\t' << p->getvalue() << endl;
	}
	
	cout << find(constList,"Re");
	
	getchar();
	return 0;
}

void predefinedConstant(list<Constant> &constList)
{
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
		if(p->getname() == n)
			return true;
	
	return false;
}
