#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include "assembler.h"

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



