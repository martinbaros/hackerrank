#include <stdio.h>
#include <cstdlib>

void update(int *a,int *b) {
    // Complete this function
    int p_a, p_b;
    p_a = *a;
    p_b = *b;
    *a = p_a+p_b;
    *b = abs(p_a-p_b);
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;

    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}
