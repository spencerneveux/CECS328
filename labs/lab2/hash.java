import java.lang.reflect.Array;

// Implements the Set ADT using a hash table with open addressing.
public class HashSet<ValueType> {
   private class Entry {
      public ValueType mValue;
      public boolean mIsNil;
   }
   
   private Node[] mTable;
   private int mCount;
   
   // Constructs a hashtable with the given size.
   public HashSet(int tableSize) {
      // TODO: see requirement #4.

      // The next line is a workaround for Java not liking us making an array
      // of a generic type. (Node is a generic type because it has generic
      // members.)
      mTable = (Node[])Array.newInstance(Node.class, tableSize); 
      // mTable's entries are all null initially.
   }
   
   // Inserts the given value into the set.
   public void add(ValueType value) {
      // Every object in Java has a .hashCode() function that computes a h(k)
      // value for that object. Use that function for your hash table index
      // calculations.
   }
   
   // Returns true if the given value is present in the set.
   public boolean find(ValueType value) {
      // Replace the following line after you write the find method.
      return false;
   }
   
   // Removes the given value from the set.
   public void remove(ValueType value) {
      
   }
   
   
}