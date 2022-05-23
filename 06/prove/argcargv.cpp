#include<stdio.h>

// argc contiene il numero dei parametri digitati
// argv è un vettore di stringhe
// ../argcargv.exe ciao luca come stai
// argv[0] = argcargv.exe\0
// argv[1] = ciao\0
// argv[argc-1] = stai\0

int main(int argc, char *argv[])
{
	int i;
	
	for(i = 0; i < argc ; i++)
		printf("%d", argv[i]);
	
	
	getchar();
	return 0;
}
