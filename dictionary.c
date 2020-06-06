#include <stdio.h>
#include <string.h>
#include <strings.h>
#include <stdlib.h>
#include <ctype.h>

int FirstLetter;
int NodeCounter = 0;
// Implements a dictionary's functionality

#include <stdbool.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    int index;
    index = hash(word);
    node *cursor = table[index];
    while (1)
    {

        if (cursor == NULL)
        {
            return false;

        }
        else if (strcasecmp(cursor->word , word) == 0)
        {
            //printf("Matched Word:%s\n",cursor->word);
            return true;
        }
        else
        {
            cursor = cursor -> next;
        }

    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    //printf("First char is :%c\n",word[0]);
    char num = (strlen(word) / 2) % N;
    //printf("Number is %i\n",num);
    //printf("Buckets:%i\n",N);
    if ((num >= N )||( num < 0 ))
        {
            printf("\n\n\n\nEXCEPTIONAL CONDITION LINE 44 ERROR\n\n\n");
            return 5555;
        }
    return num;
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    FILE *f = fopen(dictionary, "r");
    if (f == NULL)
    {
        printf("Couldn't open the Dictonaryy!\nAborting Operation");
        return false;
    }
    char TheWord[LENGTH + 1];
    int ret;
    while (true)
    {

        ret = fscanf(f,"%s",TheWord);
        if (ret == EOF)
         {
             printf("End Of File Found!");
             break;
         }
         ////printf("Word: %s\n",TheWord);
         node *n = malloc(sizeof(node));
         if (n == NULL)
         {
             printf("OUT OF MEMORY!\n");
             return false;
         }
         strcpy(n->word,TheWord);
         //printf("After STR COPY%s:\n",n->word);
         int index;
         index = hash(TheWord);
         n->next = table[index];
         table[index] = n;
         NodeCounter++;
    }
    fclose(f);
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    //printf("NodeCounter:%i",NodeCounter);
    return NodeCounter;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    node *cursor = NULL;
    node *temp = NULL;
    for (int i=0;i<N;i++)
    {
        cursor = table[i];
        if ( cursor == NULL)
        {

        }
        else
        {
            temp = cursor;
            cursor = cursor -> next;
            free(temp);
        }
    }
    return true;
}
