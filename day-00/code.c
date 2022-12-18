#include <stdio.h>
#include <string.h>

int main() {
    char name[20];

    printf("Name: ");
    scanf("%[^\n]s", name); // Anish, Anish Shobith

    if (strlen(name))
        printf("Hello, %s!", name);
    else
        printf("Hello, SJEC!");
}