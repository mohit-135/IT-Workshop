#include<stdio.h>

int main()
{
    int a,b,c;
    printf("enter first numbers :");
    scanf("%d",&a);
    printf("enter second numbers :");
    scanf("%d",&b);
    printf("enter third numbers :");
    scanf("%d",&c);

    if(a>b){
        if(a>c){
            printf("%d is the largest number",a);
        }
        else{
            printf("%d is the largest number",c);
        }
    }
    else{
        if(b>c){
            printf("%d is the largest number",b);
        }
        else{
            printf("%d is the largest number",c);
        }
    }
    return 0;
}