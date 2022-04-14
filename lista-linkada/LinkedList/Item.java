package LinkedList;

public class Item {
  private Integer value;
  public Item nextItem;

  public Item(Integer value) {
    this.value = value;
  }

  public Integer getValue() {
    return this.value;
  }

  @Override
  public String toString() {
    return value.toString();
  }
}
