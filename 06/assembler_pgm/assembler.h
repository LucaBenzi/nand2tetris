#include<stdio.h>
#include<string.h>
#include<stdlib.h>

typedef struct{
	char name[50];
	int value;
}constant;

bool hasMoreCommands(char *str , FILE* fp);	//is like the fgets funct
int commandType(char * str);

