import java.io.*;

public class PersonName {
    public static void main(String[] args) {
        try {

            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

            System.out.print("Enter your name: ");
            String name = br.readLine();

        
            System.out.println("Name: " + name);
            System.out.println("Length of name: " + name.length());

            FileWriter fw = new FileWriter("person.txt");
            fw.write(name);
            fw.close();

            System.out.println("Name stored successfully in person.txt");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
