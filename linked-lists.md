---
layout: default
---


# Linked List Exercise

In this exercise, you will implement a Linked List. We will build up to this in parts. 


<br/>

## Part 1: Familiarize Yourself with the Code

**The LinearNode Class.** Recall the `LinearNode` class from lecture:

```java
public class LinearNode<T> {
   private LinearNode<T> next;
   private T element;

   public LinearNode() {
      next = null;
      element = null;
   }

   public LinearNode(T elem) {
      next = null;
      element = elem;
   }

   public LinearNode<T> getNext() {
      return next;
   }

   public void setNext(LinearNode<T> node) {
      next = node;
   }

   public T getElement() {
      return element;
   }

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
     * Returns the element at the specified position from the list
     *
     * @param index of the element in the list
     * @return the element to be returned
     */
    public T get(int position);

    /**
     * Inserts an element at the given position in the list.
     * 
     * @param the index of the element to be added
     * @param the element to be added
     */
    public void insert(int position, T element);
    
    /**
     * Removes the element at the specified position from the list
     * 
     * @return the element to be returned
     */
    public T remove(int position);

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

**The InvalidOperationException.** Below is a class that implements an exception that should be thrown
when a client tries to do something invalid with your list:
```java
public class InvalidOperationException extends RuntimeException {
   public InvalidOperationException(String message) {
      super(message);
   }
}
```

Answer: which methods in the LinearList interface should throw this exception? Why?


<br/>

## Part 2: Creating a BlueJ Project

Create a new BlueJ project and create a `.java` file for each of the above code snippets.


<br/>

## Part 3: Implement a Linked List

Create a new class, `LinkedList<T>` that satisfies the following:
1. It uses the `LinearNode<T>` class above.
2. It `implements` the `LinearList<T>` interface above.

For brevity, we won't ask you to thoroughly test your code. However, we do recommend that you:
1. Implement the `toString` method early on.
2. Use the `toString` method to check your other methods work.

Please write pseudo-code on the whiteboards for **all methods** before implementing them in Java.


<br/>

## Part 4: Concatenation

Although your `LinkedList<T>` must implement the `LinearList<T>` interface, it can **additionally** have other methods.
Please implement an instance method, `concatenate`, that takes in a `LinkedList<T> other` as argument and:
1. Appends `other` to the end of the linked list.
2. Empties out `other`.

As before, please write pseudo-code on the whiteboards before writing code on the computer.

After implementing this method, answer: what would `concatenate` look like for an array-based list?
And is it more or less efficient than your linked-based implementation? Why?


<br/>

## Part 5: LinkedStack (Extra/Time Dependent)

We can also uses LinkedLists to implement other data structures.  Consider the Stack interface below.

Create a new class, `LinkedStack<T>` that satisfies the following:
1. It extends the `LinkedList<T>` class you previously wrote.
2. It `implements` the `Stack<T>` interface below.

As before, please write pseudo-code on the whiteboards before writing code on the computer.

**The Stack Interface.** 

```java
public interface Stack<T> {
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
     * Pushes the given element onto the stack
     *
     * @param the element to be added
     */
    public void push(T element);

    /**
     * Removes (and returns) the element on the top of the stack.
     * 
     * @return the top element from the stack (which was removed) 
     */
    public T pop();
    
    /**
     * Returns the element on the top of the stack.
     * 
     * @return the top element from the stack (which was NOT removed) 
     */
    public T peek();

    /**
     * Generates a String representation of list; 
     * first element in the representation is the front
     * 
     * @return a String representation of the list
     */
    public String toString();
}
```

<!--

<br/>

## Part 5: Create a Doubly-Linked List Node

1. Extend the `LinearNode<T>` class to create a `DoublyLinearNode<T>` class.
2. In addition to maintaining a reference to the *next* element in the list, this class should also maintain a reference to the element *previous* in the list.
3. Create the necessary getters and setters for this class, following the style of `LinearNode<T>`.


<br/>


## Part 6:  Create a Doubly-Linked List

1. Using your `DoublyLinearNode<T>`, create a new class, `DoublyLinkedList`, that implements `LinearList` interface.
2. Implemenmt *every method* listed in the interface.
3. Add a method, `removeLast`, that removes the last element of the list. You should be able to implement this *without any loops*.

-->
