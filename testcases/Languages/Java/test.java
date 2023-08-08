public class test {

  public static int factorial(int n) {
    if (n == 0) {
      return 1;
    } else {
      return n * factorial(n - 1);
    }
  }

  public static int fibonacci(int n) {
    if (n == 0) {
      return 0;
    } else if (n == 1) {
      return 1;
    } else {
      return fibonacci(n - 1) + fibonacci(n - 2);
    }
  }

  public static void main(String[] args) {
    int result1 = factorial(5);
    int result2 = fibonacci(10);
    System.out.println("factorial(5) = " + result1);
    System.out.println("fibonacci(10) = " + result2);
  }
}
