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

  private void recursiveShow(Item item) {
    if (item.nextItem != null) {
      System.out.print(item + ", ");
      this.recursiveShow(item.nextItem);
    } else {
      System.out.print(item);
    }
  }

  public void show() {
    Item item = this.firstItem;
    System.out.print('[');
    
    this.recursiveShow(item);

    System.out.println(']');
  }
}
