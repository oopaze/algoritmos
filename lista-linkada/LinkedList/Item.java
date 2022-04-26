package LinkedList;

public class Item {
  private Integer value;
  public Item nextItem;

  public Item(Integer value) {
    this.value = value;
  }

  public Item get(Integer index, Integer initialIndex) {
    if (index == initialIndex) {
      return this;
    } else if(nextItem == null) {
      String errorMessage = String.format("Index %d out of range %d", index, initialIndex);
      throw new IndexOutOfBoundsException(errorMessage);
    } else {
      return nextItem.get(index, initialIndex + 1);
    }
  }

  public void set(Integer value) {
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
