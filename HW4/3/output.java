class input {
    public static void main(String[] args) {
        try {
            int a = Integer.parseInt(args[0]);
            int b = Integer.parseInt(args[1]);
            int c = a / b;
            System.out.println("Result: " + c);
        } catch (ArithmeticException e) {
            System.out.println("Divide by zero error");
        } catch (NumberFormatException e) {
            System.out.println("Invalid input");
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Insufficient arguments");
        } catch (Exception e) {
            System.out.println("Exception message: " + e.getMessage());
        }
    }
}

class output {
    public static void main(String[] args) {
        try {
            int a = Integer.parseInt(args[0]);
            int b = Integer.parseInt(args[1]);
            int c = a / b;
            System.out.println("Result: " + c);
        } catch (ArithmeticException e) {
            System.out.println("Divide by zero error");
        } catch (NumberFormatException e) {
            System.out.println("Invalid input");
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Insufficient arguments");
        } catch (Exception e) {System.out.println("Exception message: " + e.getMessage());}
    }
}
