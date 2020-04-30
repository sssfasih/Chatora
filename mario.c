// Mario v1 for CS50 <3 - sssfasih@gmail.com

#include <stdio.h>
#include <cs50.h>

int main(void)
{
int num;
do { num = get_int("Enter Number: "); }
while (num > 8 || num < 1);


for (int a=1;a<num+1;a++){

    for (int dot =a;dot<num;dot++)
    {
        printf(" ");
    }
    for (int b=a;b>0;b--){
        printf("#");
    }
    printf("\n");
}

}