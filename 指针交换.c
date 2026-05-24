#include <stdio.h>
int main()
{
	void swap(int *p1,int*p2);
	int a,b;
	int *s1,*s2;
	scanf("%d%d",&a,&b);

	s1=&a; s2=&b;
	if (a<b)swap(s1,s2);
	printf("max=%d,min=%d",a,b);
	return 0;	

	
}
void swap(int *p1,int *p2)
{
	int p;
	p=*p1;
	*p1=*p2;
	*p2=p;
	
}
