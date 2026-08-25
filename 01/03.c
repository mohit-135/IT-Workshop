#include<stdio.h>

int main()
{
    int marks[4] , total = 0 ;
    float average , percentage;
    int size = 5;
    for (int i = 0; i < size; i++)
    {
        printf("Enter marks of subject %d : ", i + 1);
        scanf("%d", &marks[i]);
        total += marks[i];
    }
    printf("Total marks are : %d", total);
    average = (float)total / size;
    printf("\nAverage marks are : %.2f", average);
    percentage = average;
    printf("\nPercentage marks are : %.2f", percentage);
    return 0;
} 