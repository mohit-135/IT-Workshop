#include<stdio.h>

int main()
{
    int days[]= {0,31,28,31,30,31,30,31,31,30,31,30,31};
    int n;
    printf("Enter month Number : ");
    scanf("%d",&n);
    printf("the number of days in month %d is : %d ", n, days[n]);
    
    return 0;
}