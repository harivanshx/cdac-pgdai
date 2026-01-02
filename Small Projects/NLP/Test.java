// Q 3 The cats spend most of the day playing. In particular, they play if the temperature is between 25
// and 35 (inclusive). Unless it is summer, then the upper limit is 45 (inclusive) instead of 35. (5)

// - Write a method isCatPlaying that has 2 parameters
// - Method needs to return if the cat is playing, otherwise, return false.
// - 1st parameter should be of type boolean and be named summer - it represents if it is summer
// - 2nd parameter represents the temperature and is of type int with the name temperature.


public class Test {
    public static void main(String[] args) {
        System.out.println(isCatPlaying(true, 40)); // true
        System.out.println(isCatPlaying(false, 36)); // false
        System.out.println(isCatPlaying(false, 35)); // true
    }

    public static boolean isCatPlaying(boolean summer, int temperature) {
        int upperLimit = summer ? 45 : 35;
        return temperature >= 25 && temperature <= upperLimit;
    }
}

