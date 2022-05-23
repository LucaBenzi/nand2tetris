#include<stdio.h>
#include <iostream>
#include<string.h>
#include<stdlib.h>
#include <list>

typedef struct{
	char name[50];
	int value;
}constant;

void removeSpace(char *str);
void removeComment(char *str);

bool hasMoreCommands(char *str , FILE* fp);	//is like the fgets funct
int commandType(char * str);

int main()
{
FILE *fsource, *fout;
int i;
char str[200];

//Constants definition
constant R0,R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12,R13,R14,R15;
constant	SP,
			LCL,
			ARG,
			THIS,
			THAT,
			SCREEN,
			KDB;

	strcpy(R0.name,"R0");	R0.value = 0;	
	strcpy(R1.name,"R1");	R1.value = 1;
	strcpy(R2.name,"R2");	R2.value = 2;
	strcpy(R3.name,"R3");	R3.value = 3;
	strcpy(R4.name,"R4");	R4.value = 4;
	strcpy(R5.name,"R5");	R5.value = 5;
	strcpy(R6.name,"R6");	R6.value = 6;
	strcpy(R7.name,"R7");	R7.value = 7;
	strcpy(R8.name,"R8");	R8.value = 8;
	strcpy(R9.name,"R9");	R9.value = 9;
	strcpy(R10.name,"R10");	R10.value = 10;
	strcpy(R11.name,"R11");	R11.value = 11;
	strcpy(R12.name,"R12");	R12.value = 12;
	strcpy(R13.name,"R13");	R13.value = 13;
	strcpy(R14.name,"R14");	R14.value = 14;
	strcpy(R15.name,"R15");	R15.value = 15;
	
	strcpy(SP.name,"SP");			R15.value = 0;
	strcpy(LCL.name,"LCL");			R15.value = 1;
	strcpy(ARG.name,"ARG");			R15.value = 2;
	strcpy(THIS.name,"THIS");		R15.value = 3;
	strcpy(THAT.name,"THAT");		R15.value = 4;
	strcpy(SCREEN.name,"SCREEN");	R15.value = 16384;
	strcpy(KDB.name,"KDB");			R15.value = 24567;

	fsource = fopen("Mult.asm","r");
	fout = fopen("0.temp","w");
	
	//create temp file to translate
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
	
	fsource = fopen("0.temp","r");
	fout = fopen("1.temp","w");
	
	while(hasMoreCommands(str,fsource))
	{
		if(commandType(str) == 1)
		{
			int num;
			char *p;
			p = &str[1];
			num = atoi(p);
			//printf("%x\n",num);
		}
	}
	
	//remove("copy.asm");	//remove the file
	getchar();
	return 0;
}

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



