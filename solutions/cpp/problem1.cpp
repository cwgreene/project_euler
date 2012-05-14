#include <stdio.h>
int main(){
    int sum = 0;
    for(int i = 1; i < 1000; i++){
        if(i % 5 && i % 3)
            continue;
        sum += i;
    }
    printf("%d\n", sum);
}
