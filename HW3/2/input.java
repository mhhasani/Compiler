public class NestedLoopsExample {
    public static void main(String[] args) {

        // For loop
        for (int i = 1; i <= 3; i++) {

            // While loop
            int j = 1;
            while (j <= 2) {

                // While loop
                int k = 1;
                while (k <= 3) {
                    System.out.println("i = " + i + ", j = " + j + ", k = " + k);
                    k++;
                    // for loop
                    for (int l = 1; l <= 2; l++) {
                        System.out.println("i = " + i + ", j = " + j + ", k = " + k + ", l = " + l);
                    }
                }

                j++;
            }

        }

        // for loop
        for (int i = 1; i <= 3; i++) {
            System.out.println("i = " + i);
            for (int j = 1; j <= 2; j++) {
                System.out.println("i = " + i + ", j = " + j);
                for (int k = 1; k <= 3; k++) {
                    System.out.println("i = " + i + ", j = " + j + ", k = " + k);
                    for (int l = 1; l <= 2; l++) {
                        System.out.println("i = " + i + ", j = " + j + ", k = " + k + ", l = " + l);
                        for (int m = 1; m <= 3; m++) {
                            System.out.println("i = " + i + ", j = " + j + ", k = " + k + ", l = " + l + ", m = " + m);
                        }
                    }
                }
            }
        }

    }
}
