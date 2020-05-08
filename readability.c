#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <math.h>

int main(void)
{

    string text = get_string("Enter text here: ");

// main for loop
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

    float L = ( lettercount / (words + 1 ) )*100;
    float S = ( sentence / (words + 1 ) )*100;
    float index = 0.0588 * L - 0.296 * S - 15.8;
    int grade = round(index);
//    printf("L: %f     S: %f",L,S);

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
        printf("Grade %d\n",grade);
    }
}