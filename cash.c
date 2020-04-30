// Cash Program CS50 <3 - sssfasih@gmail.com

#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{

// Variable Declaration
    float input;
    int cents;
    int coins = 0;
// do while to add limitation that no negative number can proceed
//Taking Input and converting into cents ; also applying round function
    do
    {
        input = get_float("Change Owed: ");
    }
    while (input <= 0);

    cents = round(input * 100);

//    printf("Total Cents: %i \n", cents);  //line to debug

//while owed amount is left : IF-ELSE ladder
    while (cents > 0)
    {
        if (cents >= 25)
        {
            cents = cents - 25;
            coins++;
        }
        else if (cents >= 10)
        {
            cents = cents - 10;
            coins++;
        }
        else if (cents >= 5)
        {
            cents = cents - 5;
            coins++;
        }
        else if (cents >= 1)
        {
            cents = cents - 1;
            coins++;
        }

    }
    // Output:
    printf("%i\n", coins);
}