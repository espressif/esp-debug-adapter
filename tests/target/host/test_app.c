#include <stdio.h>

extern int print_hamlet(void);

int main()
{
    int lines = print_hamlet();
    printf("\n[Printed lines of the play: %d]\n", lines );
    printf("[Bye!]\n");
    while(1);
    return 0;
}