#include <stdio.h>
#include <cs50.h>  // for get_string function
#include <string.h> // for strlen function
#include <math.h>  // for round function

int main(void)
{

    string text = get_string("Enter text here: ");

// MAIN FOR LOOP
    int lettercount = 0;
    float words = 0;
    int sentence = 0;
    string result = NULL;
    for (int loop = 0, max = strlen(text); loop < max; loop++)
    {
        if ((text[loop] >= 'a' && text[loop] <= 'z') || (text[loop] >= 'A' && text[loop] <= 'Z'))
        {
            lettercount++;
        }

        if (text[loop] == ' ')
        {
            words++;
        }

        if (text[loop] == '.' || text[loop] == '!' || text[loop] == '?')
        {
            sentence++;
        }
    }
    /*    printf("Letters: %i \n", lettercount);
        printf("Words: %f \n", words+1); //Added 1 because last word don't end at space character.
        printf("Sentences: %i \n",sentence);
    */

// CALCULATING ACCORDING TO FORMULA
    float L = (lettercount / (words + 1)) * 100;
    float S = (sentence / (words + 1)) * 100;
    float index = 0.0588 * L - 0.296 * S - 15.8;
    int grade = round(index);
//    printf("L: %f     S: %f",L,S);


// FINAL PRINT STATMENT FOR RESULT
    if (grade >= 16)
    {

        printf("Grade 16+\n");
    }
    else if (grade < 1)
    {

        printf("Grade Before Grade 1\n");
    }
    else
    {
        printf("Grade %d\n", grade);
    }
}