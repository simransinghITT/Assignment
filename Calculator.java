public class Calculator {
   public static void main(String[] args) {
      double $num1;
      double $num2;
      double ans;
      char $op;
      switch($op) {
         case '+': ans = $num1 + $num2;
            break;
         case '-': ans = $num1 - $num2;
            break;
         case '*': ans = $num1 * $num2;
            break;
         case '/': ans = $num1 / $num2;
            break;
         default:  System.out.printf("Error! Enter correct operator");
            return;
      }
      System.out.print("\nThe result is given as follows:\n");
      System.out.printf($num1 + " " + $op + " " + $num2 + " = " + ans);
   }
}
