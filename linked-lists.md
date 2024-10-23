---
layout: default
---


# Linked List Exercise

In this exercise, you will implement a Stack using a Linked List. We will build up to this in parts.


## Part 1: Familiarize Yourself with the Code

**The LinearNode Class.** Recall the `LinearNode` class from lecture:

```java
public class LinearNode<T> {
   private LinearNode<T> next;
   private T element;

   //-----------------------------------------------------------------
   //  Creates an empty node.
   //-----------------------------------------------------------------
   public LinearNode() {
      next = null;
      element = null;
   }

   //-----------------------------------------------------------------
   //  Creates a node storing the specified element.
   //-----------------------------------------------------------------
   public LinearNode(T elem) {
      next = null;
      element = elem;
   }

   //-----------------------------------------------------------------
   //  Returns the node that follows this one.
   //-----------------------------------------------------------------
   public LinearNode<T> getNext() {
      return next;
   }

   //-----------------------------------------------------------------
   //  Sets the node that follows this one.
   //-----------------------------------------------------------------
   public void setNext(LinearNode<T> node) {
      next = node;
   }

   //-----------------------------------------------------------------
   //  Returns the element stored in this node.
   //-----------------------------------------------------------------
   public T getElement() {
      return element;
   }

   //-----------------------------------------------------------------
   //  Sets the element stored in this node.
   //-----------------------------------------------------------------
   public void setElement(T elem) {
      element = elem;
   }
}
```

For this class:
* What does `element` represent?
* What does `next` represent?
* Why is the type of `next` also a `LinearNode<T>`?
* What is `T` used for?


**The LinearList Interface.** Next, consider the interface below:

```java
public interface LinearList<T> {
    /**
     * Checks if the list is empty
     * 
     * @return true if the list is empty, false otherwise
     */
    public boolean isEmpty();
    
    /**
     * Returns the size of the list
     * 
     * @return the size (or length) of the list
     */
    public int size();
    
    /**
     * Adds an element at the rear (or end) of the list
     * 
     * @param the element to be added
     */
    public void addLast(T element);
    
    /**
     * Adds an element at the front (or beginning) of the list
     * 
     * @param the element to be added
     */
    public void addFirst(T element);
    
    /**
     * Removes the element at the head (or front) of the list
     * 
     * @return the element to be returned
     */
    public T remove();
    
    /**
     * Generates a String representation of list; 
     * first element in the representation is the front
     * 
     * @return a String representation of the list
     */
    public String toString();
}
```

Then, answer:
* What are interfaces used for?
* What does it mean to create an object that `implements` this interface?

**The EmptyCollectionException.** Below is a class that implements an exception that should be thrown
when a client tries to operate on an empty collection.
* Which methods in the LinearList interface should throw this exception? Why?
```java
public class EmptyCollectionException extends RuntimeException {
   //------------------------------------------------------------------
   //  Sets up this exception with an appropriate message.
   //------------------------------------------------------------------
   public EmptyCollectionException (String message)
   {
      super (message);
   }
}
```

## Part 2: Creating a BlueJ Project

Create a new BlueJ project and create a `.java` file for each of the above code snippets.


## Part 3: Implement a Linked List

Create a new class, `LinkedList<T>` that satisfies the following:
1. It uses the `LinearNode<T>` class above.
2. It `implements` the `LinearList<T>` interface above.

For brevity, we won't ask you to thoroughly test your code. However, we do recommend that you:
1. Implement the `toString` method early on.
2. Use the `toString` method to check your other methods work.


## Part 4: Implement a Stack using a Linked List

Below is the `Stack` interface:

```java
public interface Stack<T> {
   //  Adds the specified element to the top of the stack.
   public void push (T element);

   //  Removes and returns the top element from the stack.
   public T pop();

   //  Returns a reference to the top element of this stack
   //  without removing it.
   public T peek();

   //  Returns true if the stack contains no elements and false
   //  otherwise.
   public boolean isEmpty();

   //  Returns the number of elements in the stack.
   public int size();

   //  Returns a string representation of the stack.
   public String toString();
}
```

Add this interface to your BlueJ project. Then, create a class, `LinkedStack<T>`, that:
1. Implements this interface.
2. Uses your `LinkedList<T>` class.

