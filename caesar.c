#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string vector[])
{
    int intigerLen(unsigned x);
    int key;
    // works only if arguments are 2
    if (argc == 2)
    {

        // if there are 2 args and after conversion to int, int length == arg1 length is True: Proceed
        key = atoi(vector[1]);
        if (intigerLen(key) == strlen(vector[1]))
        {

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
                    if (isupper(input[loop]))
                    {
                        printf("%c", ((((input[loop] + key) - 65) % 26)) + 65);
                    }
                    else if (islower(input[loop]))
                    {
                        printf("%c", ((((input[loop] + key) - 97) % 26)) + 97);
                    }
                    else
                    {
                        printf("INVALID INPUT");
                        return 1;
                    }
                }
                else
                {
                    printf("%c", input[loop]);
                }

            }
            printf("\n");
        }

        // this else condition is connected to second if statement where int len is compared to str length
        else
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }



    }
    // this else condition is connected to first if where argument 2 condition is given.
    else
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    //when everything worked fine. return zero!
    return 0;
}

// Function that returns intiger length
int intigerLen(unsigned x)
{

    if (x >= 10000)
    {
        return 5;
    }

    if (x >= 1000)
    {
        return 4;
    }
    if (x >= 100)
    {
        return 3;
    }
    if (x >= 10)
    {
        return 2;
    }
    else
    {
        return 1;
    }
}