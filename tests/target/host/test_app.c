#include <stdio.h>

int print_hamlet(void){
    int lines = 0;
    lines++;
    printf("HAMLET\n");
    lines++;
    printf("\n");
    lines++;
    printf("O, I die, Horatio;\n");
    lines++;
    printf("The potent poison quite o'er-crows my spirit:\n");
    lines++;
    printf("I cannot live to hear the news from England;\n");
    lines++;
    printf("But I do prophesy the election lights\n");
    lines++;
    printf("On Fortinbras: he has my dying voice;\n");
    lines++;
    printf("So tell him, with the occurrents, more and less,\n");
    lines++;
    printf("Which have solicited. The rest is silence.\n");
    lines++;
    printf("\n");
    lines++;
    printf("Dies\n");
    return lines;
}

int main()
{
    int lines = print_hamlet();
    printf("\n[Printed lines of the play: %d]\n", lines );
    printf("[Bye!]\n");
    return 0;
}