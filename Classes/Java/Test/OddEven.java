import java.util.*;


class OddEven{
    public static void main(String[] args) {
        
              Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();

        if (num % 2 == 0){
            System.err.println("Even");

        }
        else{
             System.err.println("Odd");
        }


    }
}