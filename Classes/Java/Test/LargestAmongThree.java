class LargestAmongThree {
    public static void main(String[] args) {
        int a = 242;
        int b = 44;
        int c = 332;

        if (a >= b && a >= c) {
            System.out.println("A is greatest");
        } else if (b >= a && b >= c) {
            System.out.println("B is greatest");
        } else {
            System.out.println("C is greatest");
        }
    }
}
