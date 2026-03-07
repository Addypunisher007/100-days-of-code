#include <stdio.h>

int main() {

    int n, i;
    int factorial = 1;

    printf("Enter a number = ");
    scanf("%d", &n);

    if(n < 1){
        printf("Entered number cannot be less than 1");
    } else{

    for(i = 1; i <= n; i++) {
        factorial = factorial * i;
    }

    printf("Factorial of %d = %d\n", n, factorial);

    return 0;
    }
}