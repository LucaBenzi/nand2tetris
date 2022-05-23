#include<stdio.h>
#include<string.h>

void removeSpace(char *str);

int main(void)
{
char prova[200];

	strcpy(prova,"ciao luca come stai       ?");
	printf("%d",strlen(prova));
	printf("%s", prova);
	removeSpace(prova);
	printf("\n%s",prova);
	
	getchar();
	return 0;
}

void removeSpace(char *str)		//perfetta: rimuove spazi dalla stringa
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
