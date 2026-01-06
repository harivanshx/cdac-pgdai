public class WeekTemperature {
    public static void main(String[] args) {

        int[] temp = {30, 32, 35, 33, 36, 34, 31};
        String[] days = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};

        int max = temp[0];
        int index = 0;

        for (int i = 1; i < temp.length; i++) {
            if (temp[i] > max) {
                max = temp[i];
                index = i;
            }
        }

        System.out.println("Highest Temperature: " + max);
        System.out.println("Day: " + days[index]);
    }
}
