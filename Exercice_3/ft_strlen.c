#include <stdio.h>
#include <string.h>

/**
* my_strlen - reproduce the behavor of strlen that calculate the length of a string
*
* @str: a pointer to the string str
*
* Return: 0 if it's an empty str, or the length (size) of str
*/
int my_strlen(char *str) {
    int length = 0;
    while (*str != '\0') {
        length++;
        str++;
    }
    return length;
}

int main(void) {
    char str[200];

    printf("Enter a non-empty string: ");
    scanf("%199s", str);
    if (str[0] == '\0') {
        printf("\n u entered an empty string");
        return (0);
    }

    int len = my_strlen(str);

    printf("Length of the string: %d\n", len);
    return (0);
}
