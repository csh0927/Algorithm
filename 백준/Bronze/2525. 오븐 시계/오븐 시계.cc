#include<stdio.h>
int main()
{
	int a, b, c;
	scanf("%d %d\n%d", &a, &b, &c);
	int d = (a + (b + c) / 60);
	int e = (b + c);
	if (a < d && d >= 24)
		printf("%d %d", d % 24, (b + c) % 60);
	else if (a < d)
		printf("%d %d", d, (b + c) % 60);
	else if (a == d)
		printf("%d %d", a, e);
}