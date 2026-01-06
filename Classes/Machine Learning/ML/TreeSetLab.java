Student.java
public class Student {

    int rollno;
    String sname;
    String address;

    // Constructor to initialize fields
    public Student(int rollno, String sname, String address) {
        this.rollno = rollno;
        this.sname = sname;
        this.address = address;
    }

    // Display method
    public void display() {
        System.out.println("Roll No: " + rollno);
        System.out.println("Name: " + sname);
        System.out.println("Address: " + address);
        System.out.println("----------------------");
    }
}

// Main Class



import java.util.LinkedList;
import java.util.Iterator;
import java.util.Scanner;

public class StudentLinkedList {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        LinkedList<Student> list = new LinkedList<>();

        // Taking input for 5 students
        for (int i = 1; i <= 5; i++) {
            System.out.println("Enter details of Student " + i);

            System.out.print("Roll No: ");
            int roll = sc.nextInt();
            sc.nextLine(); // consume newline

            System.out.print("Name: ");
            String name = sc.nextLine();

            System.out.print("Address: ");
            String address = sc.nextLine();

            Student s = new Student(roll, name, address);
            list.add(s);
        }

        // Display using Iterator
        System.out.println("\n--- Student Details ---");
        Iterator<Student> itr = list.iterator();

        while (itr.hasNext()) {
            Student s = itr.next();
            s.display();
        }
    }
}