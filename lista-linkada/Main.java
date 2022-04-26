import LinkedList.List;

public class Main {
  public static void main(String[] args) {
    List numbers_list = new List();

    numbers_list.addItem(2);
    numbers_list.addItem(3);
    numbers_list.addItem(4);

    System.out.println(numbers_list);
    System.out.println(numbers_list.get(1));

    numbers_list.set(2, 10);

    System.err.println(numbers_list);
  }
}