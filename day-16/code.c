#include <stdio.h>

int main() {
    int n, m;
    scanf("%d %d", &n, &m);

    int c[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &c[i]);
    }

    int max = 0;
    int start = 0;

    for (int i = 0; i <= n - m; i++) {
        int total = 0;
        for (int j = 0; j < m; j++) {
            total += c[i + j];
        }

        if (total > max) {
            max = total;
            start = i;
        }
    }

    printf("%d\n", max);

    return 0;
}