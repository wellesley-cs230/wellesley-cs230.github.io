---
layout: default
---

# Linked List Exercise

In this exercise, you will implement a Linked List. We will build up to this in parts.

For this exercise, assume that elements added to the list or stack are not `null`.

<br/>

## Part 1: Familiarize Yourself with the Code

### The LinearNode Class

Recall the `LinearNode` class from lecture:

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

### The LinearList Interface

Next, consider the interface below:

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
     * Returns the element at the specified position in the list.
     *
     * Positions start at 0. If position is less than 0 or greater than
     * or equal to size(), return null.
     *
     * @param position the 0-indexed position of the element
     * @return the element at the specified position, or null if the
     *         position is not valid
     */
    public T get(int position);

    /**
     * Inserts an element at the given 0-indexed position in the list.
     *
     * Valid positions range from 0 through size(), inclusive. Inserting
     * at position size() adds the element to the end of the list.
     *
     * If position is less than 0 or greater than size(), do not change
     * the list.
     *
     * @param position the position at which to insert the element
     * @param element the element to be added
     */
    public void insert(int position, T element);

    /**
     * Removes the element at the specified 0-indexed position from the list.
     *
     * Positions start at 0. If position is less than 0 or greater than
     * or equal to size(), return null and do not change the list.
     *
     * @param position the position of the element to remove
     * @return the removed element, or null if the position is not valid
     */
    public T remove(int position);

    /**
     * Generates a String representation of the list.
     *
     * The first element in the representation is the front of the list.
     * Use square brackets, with elements separated by commas and spaces.
     *
     * Examples:
     *
     * An empty list: []
     * A list containing 10, 20, and 30: [10, 20, 30]
     *
     * @return a String representation of the list
     */
    public String toString();
}
```

Then, answer:

* What are interfaces used for?
* What does it mean to create an object that `implements` this interface?
* Which positions are valid for `get`?
* Which positions are valid for `remove`?
* Which positions are valid for `insert`?
* What should happen when `get` receives an invalid position?
* What should happen when `remove` receives an invalid position?
* What should happen when `insert` receives an invalid position?

<br/>

## Part 2: Creating a BlueJ Project

Create a new BlueJ project and create a `.java` file for each of the following:

* `LinearNode`
* `LinearList`
* `LinkedList`

<br/>

## Part 3: Implement a Linked List

Create a new class, `LinkedList<T>`, that satisfies the following:

1. It uses the `LinearNode<T>` class above.
2. It `implements` the `LinearList<T>` interface above.
3. It has a no-argument constructor that creates an empty list.
4. It follows all of the behaviors described in the comments in the `LinearList<T>` interface.

For brevity, we will not ask you to thoroughly test your code. However, we do recommend that you:

1. Implement the `toString` method early on.
2. Use the `toString` method to check that your other methods work.
3. Test both valid and invalid positions.
4. Test inserting into an empty list.
5. Test removing the first element.
6. Test removing the last element.
7. Test removing the only element from a list.

Please write pseudo-code on the whiteboards for **all methods** before implementing them in Java.

<br/>

## Part 4: Concatenation

Although your `LinkedList<T>` must implement the `LinearList<T>` interface, it can **additionally** have other methods.

Please implement an instance method, `concatenate`, that takes a `LinkedList<T> other` as an argument and:

1. Appends all of the elements in `other` to the end of the current list.
2. Preserves the order of the elements in `other`.
3. Makes `other` empty after the operation.
4. Leaves the current list unchanged if `other` is `null`.
5. Does nothing if `other` is the same list as the current list.

For example, if:

```text
this list: [1, 2, 3]
other:     [4, 5]
```

then, after calling:

```java
thisList.concatenate(other);
```

the lists should be:

```text
this list: [1, 2, 3, 4, 5]
other:     []
```

As before, please write pseudo-code on the whiteboards before writing code on the computer.

After implementing this method, answer:

* What would `concatenate` look like for an array-based list?
* Is it more or less efficient than your linked-based implementation? Why?

<br/>

## Part 5: LinkedStack (Extra/Time Dependent)

We can also use linked lists to implement other data structures. Consider the `Stack` interface below.

Create a new class, `LinkedStack<T>`, that satisfies the following:

1. It has a `LinkedList<T>` object as a field.
2. It uses that `LinkedList<T>` object to store the stack elements.
3. It `implements` the `Stack<T>` interface below.
4. The front of the linked list is the top of the stack.
5. It has a no-argument constructor that creates an empty stack.

Question: Why would you **not** want to use an "is-a" relationship here?

For this exercise, assume that elements passed to `push` are not `null`.

### The Stack Interface

```java
public interface Stack<T> {
    /**
     * Checks if the stack is empty
     *
     * @return true if the stack is empty, false otherwise
     */
    public boolean isEmpty();

    /**
     * Returns the size of the stack
     *
     * @return the size of the stack
     */
    public int size();

    /**
     * Pushes the given element onto the stack.
     *
     * The new element becomes the top element.
     *
     * @param element the element to be added
     */
    public void push(T element);

    /**
     * Removes and returns the element on the top of the stack.
     *
     * If the stack is empty, return null.
     *
     * @return the top element from the stack, or null if the stack is empty
     */
    public T pop();

    /**
     * Returns the element on the top of the stack without removing it.
     *
     * If the stack is empty, return null.
     *
     * @return the top element from the stack, or null if the stack is empty
     */
    public T peek();

    /**
     * Generates a String representation of the stack.
     *
     * The first element in the representation is the top of the stack.
     *
     * @return a String representation of the stack
     */
    public String toString();
}
```

As before, please write pseudo-code on the whiteboards for all methods before writing code on the computer.

<!--

<br/>

## Part 6: Create a Doubly-Linked List

1. Extend the `LinearNode<T>` class to create a `DoublyLinearNode<T>` class.
2. In addition to maintaining a reference to the *next* element in the list, this class should also maintain a reference to the element *previous* in the list.
3. Create the necessary getters and setters for this class, following the style of `LinearNode<T>`.

<br/>

## Part 7: Create a Doubly-Linked List

1. Using your `DoublyLinearNode<T>`, create a new class, `DoublyLinkedList`, that implements the `LinearList` interface.
2. Implement *every method* listed in the interface.
3. Add a method, `removeLast`, that removes the last element of the list. You should be able to implement this *without any loops*.

-->