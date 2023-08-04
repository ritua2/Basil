#include <stdio.h>

int factorial(int n) {
  if (n == 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

int fibonacci(int n) {
  if (n == 0) {
    return 0;
  } else if (n == 1) {
    return 1;
  } else {
    return fibonacci(n - 1) + fibonacci(n - 2);
  }
}

int main() {
  int result1 = factorial(5);
  int result2 = fibonacci(10);
  printf("factorial(5) = %d\n", result1);
  printf("fibonacci(10) = %d\n", result2);
  return 0;
}
