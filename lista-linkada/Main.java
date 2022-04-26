import LinkedList.List;

public class Main {
  public static void main(String[] args) {
    List numbers_list = new List();

    numbers_list.append(2);
    numbers_list.append(3);
    numbers_list.append(4);
    numbers_list.append(1);
    numbers_list.append(20);
    numbers_list.append(13);

    System.out.println("List = " + numbers_list);
    System.out.println("Index One = " + numbers_list.get(1));

    numbers_list.set(2, 10);

    System.err.println("Updated List = " + numbers_list);
    System.out.println("Removed Item = " + numbers_list.remove(1));
    System.err.println("Updated List = " + numbers_list);
  }
}