class Vehicles {
    protected String name;
    protected String color;
    
    public Vehicles(String name, String color) {
        this.name = name;
        this.color = color;
    }
    
    public void display() {
        System.out.println("Name: " + name + ", Color: " + color);
    }
}

class Automobiles extends Vehicles {
    protected String fuelType;
    
    public Automobiles(String name, String color, String fuelType) {
        super(name, color);
        this.fuelType = fuelType;
    }
    
    @Override
    public void display() {
        super.display();
        System.out.println("Fuel: " + fuelType);
    }
}

class Car extends Automobiles {
    private int doors;
    
    public Car(String name, String color, String fuelType, int doors) {
        super(name, color, fuelType);
        this.doors = doors;
    }
    
    @Override
    public void display() {
        super.display();
        System.out.println("Doors: " + doors + "\n");
    }
}

class Bus extends Automobiles {
    private int capacity;
    
    public Bus(String name, String color, String fuelType, int capacity) {
        super(name, color, fuelType);
        this.capacity = capacity;
    }
    
    @Override
    public void display() {
        super.display();
        System.out.println("Capacity: " + capacity + "\n");
    }
}

class PulledVehicles extends Vehicles {
    protected String pulledBy;
    
    public PulledVehicles(String name, String color, String pulledBy) {
        super(name, color);
        this.pulledBy = pulledBy;
    }
    
    @Override
    public void display() {
        super.display();
        System.out.println("Pulled By: " + pulledBy);
    }
}

class Cart extends PulledVehicles {
    private double capacity;
    
    public Cart(String name, String color, String pulledBy, double capacity) {
        super(name, color, pulledBy);
        this.capacity = capacity;

    }
    
    @Override
    public void display() {
        super.display();
        System.out.println("Capacity: " + capacity + " kg\n");
    }
}

class Rickshaw extends PulledVehicles {
    private int passengers;
    
    public Rickshaw(String name, String color, String pulledBy, int passengers) {
        super(name, color, pulledBy);
        this.passengers = passengers;
    }
    
    @Override
    public void display() {
        super.display();
        System.out.println("Passengers: " + passengers + "\n");
    }
}

public class Hierarchy {
    public static void main(String[] args) {
        Car car = new Car("Toyota", "White", "Diesel", 4);
        Bus bus = new Bus("Ashok", "Yellow", "Diesel", 50);
        Cart cart = new Cart("Cart", "Brown", "Horse", 500);
        Rickshaw rickshaw = new Rickshaw("Rickshaw", "Red", "Human", 2);
        
        car.display();
        bus.display();
        cart.display();
        rickshaw.display();
    }
}
