// Mario v1 for CS50 <3 - sssfasih@gmail.com

#include <stdio.h>
#include <cs50.h>

int main(void)
{

// first execution condition : Must rejecct negative ,zero and above 8 numbers
int num;
do { num = get_int("Enter Number: "); }
while (num > 8 || num < 1);

// simple loop from one to end for new line
for (int a=1;a<num+1;a++){

    //loop that prints empty space
    for (int dot =a;dot<num;dot++)
    {
        printf(" ");
    }
    // negative loop that prints # until point 0 is reached
    for (int b=a;b>0;b--){
        printf("#");
    }
    //new line statement is in the first loop
    printf("\n");
}

}