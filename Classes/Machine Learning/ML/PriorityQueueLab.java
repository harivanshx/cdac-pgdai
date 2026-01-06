import java.util.PriorityQueue;
import java.util.Comparator;

public class PriorityQueueLab {

    public static void main(String[] args) {

        // Comparator to sort items by priority (lower number = higher priority)
        Comparator<Item> priorityComparator = new Comparator<Item>() {
            @Override
            public int compare(Item i1, Item i2) {
                return Integer.compare(i1.getPriority(), i2.getPriority());
            }
        };

        PriorityQueue<Item> queue = new PriorityQueue<>(priorityComparator);

        queue.add(new Item("Task A", 3));
        queue.add(new Item("Task B", 1));
        queue.add(new Item("Task C", 2));

        while (!queue.isEmpty()) {
            System.out.println(queue.poll());
        }
    }
}
