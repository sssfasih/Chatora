#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

int FirstLetter;
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
const unsigned int N = 25;

// Hash table
node *table[N];

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    // TODO
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    //printf("First ELemt is :%c\n",word[0]);
    char num = tolower(word[0] - 97);
    printf("Number is %i\n",num);
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
         printf("Word: %s\n",TheWord);
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
    }
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return 0;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    // TODO
    return false;
}
