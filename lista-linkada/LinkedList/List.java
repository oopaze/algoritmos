package LinkedList;

public class List {
  private Item firstItem;
  private Item lastItem;
  
  Integer length = 0;
  
  public void addItem(Integer value) {
    Item newItem = new Item(value); 

    if(firstItem == null) {
      this.firstItem = newItem;
      this.lastItem = newItem;
    } else {
      this.lastItem.nextItem = newItem;
      this.lastItem = newItem;
    }

    length += 1;
  }

  public Item get(Integer index) {
    return this.firstItem.get(index, 0);
  }

  public void set(Integer index, Integer value) {
    Item item = this.firstItem.get(index, 0);
    item.set(value);
  }

  public void show() {
    System.out.println(this);
  }

  private String recursiveShow(Item item) {
    if (item.nextItem != null) {
      return item.toString() + ", " + this.recursiveShow(item.nextItem);
    } else {
      return item.toString();
    }
  }

  @Override
  public String toString() {
    Item item = this.firstItem;
    String listAsString = "[";
    
    listAsString += this.recursiveShow(item);

    listAsString += "]";

    return listAsString;
  }
}
