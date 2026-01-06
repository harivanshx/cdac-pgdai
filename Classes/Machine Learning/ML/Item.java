public class Item {
    private String name;
    private int priority;

    public Item(String name, int priority) {
        this.name = name;
        this.priority = priority;
    }

    public int getPriority() {
        return priority;
    }

    public String getName() {
        return name;
    }

    @Override
    public String toString() {
        return "Item{name='" + name + "', priority=" + priority + "}";
    }
}
