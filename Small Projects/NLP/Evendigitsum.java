// Q 4 Write a method named getEvenDigitSum with one parameter of type int called number (5)
// - The method should return the sume of the even digits within the number
// - If the number is negative, the method should return -1 to indicate an invalid value


public class Evendigitsum {
    public static void main(String[] args) {
        System.out.println(getEvenDigitSum(123456)); // 12
        System.out.println(getEvenDigitSum(252)); // 4
        System.out.println(getEvenDigitSum(-22)); // -1
    }

    public static int getEvenDigitSum(int number) {
        if (number < 0) {
            return -1;
        }
        int sum = 0;
        while (number > 0) {
            int digit = number % 10;
            if (digit % 2 == 0) {
                sum += digit;
            }
            number /= 10;
        }
        return sum;
    }
}
    