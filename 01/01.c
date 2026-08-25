#include<stdio.h>
#include<math.h>

int power(int a ,int b){
    if (b == 1){
        return a;
    }
    else{
        return a * power(a,b-1);
    }
}
int main(){
    int a , b;
    printf("enter number one :");
    scanf("%d",&a);
    printf("enter number two :");
    scanf("%d",&b);
    
    printf("The sum is : %d",a+b);
    printf("\nThe difference is : %d",a-b);
    printf("\nThe product is : %d",a*b);
    printf("\nThe division is : %d",a/b);
    printf("\nThe remainder is : %d",a%b);
    printf("\nThe float is: %f ",(float)a/b);
    printf("\n%d to the power %d is : %d",a , b, power(a,b));
    return 0;
}