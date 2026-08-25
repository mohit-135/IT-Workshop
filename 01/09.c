#include<stdio.h>

int power(int a ,int b){
    if (b == 1){
        return a;
    }
    else{
        return a * power(a,b-1);
    }
}
int main()
{
    int a , b;
    printf("enter number one :");
    scanf("%d",&a);
    printf("enter number two :");
    scanf("%d",&b);
    printf("the result of %d raised to the power %d is %d", a, b, power(a,b));
    return 0;
}