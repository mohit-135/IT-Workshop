#include <stdio.h>

int main(){
    int a,b,c;

    printf("Enter sides of the triangle: ");
    scanf("%d %d %d",&a,&b,&c);

    if(a==b && b==c && a==c){
        printf("the triangle is an equilateral ");

    }else if(a==b || b==c || a==c){
        printf("the triangle is an isosceles ");

    }else {
        printf("the triangle is an scalen ");

    }
}