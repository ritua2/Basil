#include <iostream>

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
  std::cout << "factorial(5) = " << result1 << std::endl;
  std::cout << "fibonacci(10) = " << result2 << std::endl;
  return 0;
}
