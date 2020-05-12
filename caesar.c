#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string vector[])
{
    // works only if arguments are 2
    if (argc == 2)
    {
        int key = atoi(vector[1]);
        // if argument is 2 but not integer already return 1 and print Usage format
        if (key == 0)

        {

            printf("Usage: ./caesar key\n");
            return 1;


        }

        //printing key for debugging
        //printf("Key is : %i \n", key);

        string input = get_string("Enter Text:");
        printf("ciphertext: ");

        // This loops iterates for each character in string array
        for (int loop = 0; loop < strlen(input); loop++)
        {
            //if iterated element is alphabet. add key else print as it is.
            if (isalpha(input[loop]))
            {

                printf("%c", (input[loop] + key) );

            }
            else
            {
                printf("%c", input[loop]);
            }

        }
        printf("\n");



    }

    // this else condition is connected to first if where argument 2 condition is given.
    else
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
}