#include<stdio.h>
int main()
{
void link_string(char*arr1,char*arr2);
char a[40]="I am a teacher";
char b[]="You are a student";

char *p1=a, *p2=b;
printf("string a:%s\nstring b:%s\n",p1,p2);
link_string(p1,p2);
printf("Now,string a:%s\nstring b:%s\n",a,b);
return 0;
}
void link_string(char *arr1,char *arr2)
{ int i;
for(i=0;*arr1!='\0';i++)
	arr1++;
for(;*arr2!='\0';arr1++,arr2++)
	*arr1=*arr2;
*arr1='\0';	
}
