package LinkedList;

public class List {
  private Item firstItem;
  private Item lastItem;
  
  Integer length = 0;
  
  public void append(Integer value) {
    Item newItem = new Item(value); 

    if(firstItem == null) {
      this.firstItem = newItem;
      this.lastItem = newItem;
    } else {
      this.lastItem.nextItem = newItem;
      this.lastItem = newItem;
    }

    this.length += 1;
  }

  public Item get(Integer index) {
    return this.firstItem.get(index);
  }

  public void set(Integer index, Integer value) {
    Item item = this.firstItem.get(index);
    item.set(value);
  }

  public Item remove(Integer index) {
    if (index >= this.length || index < 0) {
      String errorMessage = String.format("Could not find index %d of length %d", index, this.length - 1);
      throw new IndexOutOfBoundsException(errorMessage);
    }
    
    Item removedItem = this.firstItem.get(index);

    if (index == 0) {
      this.firstItem = removedItem.nextItem;
    } else {
      Item lastItem = this.firstItem.get(index - 1);
      lastItem.nextItem = removedItem.nextItem;
    }
    this.length -= 1;
    return removedItem;
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
