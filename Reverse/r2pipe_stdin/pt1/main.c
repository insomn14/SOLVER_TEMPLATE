#include <stdio.h>

int main()
{
	char buf[254];
	printf("[?] Password : ");
	fgets(buf, 254, stdin);
	printf("[*] INPUT : %s", buf);
	return 0;
}
