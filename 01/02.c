#include<stdio.h>

int main()
{
    int n;
    printf("enter a three digit number : ");
    scanf("%d",&n);
    printf("The reverse of the number is : ");
    while(n>0)
    {
        printf("%d",n%10);
        n=n/10;
    }
    return 0;
}