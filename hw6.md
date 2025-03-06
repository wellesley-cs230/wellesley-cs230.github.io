---
layout: default
---


# Homework 6, Part A: Doubly Linked Lists

Here, you will create your own implementation of a doubly linked list.
A doubly linked list is a linked list in which every node maintains a reference to the item next in the list,
**as well as** the item previous in the list.

<img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fbrianross-95869.medium.com%2Fdoubly-linked-lists-double-the-trouble-but-double-the-fun-1d13ed215dfe&psig=AOvVaw08dqXLXzd6giBQ4HaCPHGW&ust=1741312229178000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCODf-92r9IsDFQAAAAAdAAAAABAE" />


## Task 0: Getting Settled

Copy over the `LinearList<T>` interface from the [in-class exercise](/linked-lists).
Your linked list should implement this interface.


## Task 1: Doubly Linear Node

Create a class, `DoublyLinearNode<T>`, to represent a node in your linked list.
You can follow the `LinearNode` from the [in-class exercise](/linked-lists) for inspiration.


## Task 2: Implementing the Doubly Linked list

Create a class, `DoublyLinkedList<T>` that uses your `DoublyLinearNode<T>` to implement the `LinearList<T>` interface.


## Task 3: Testing

Please test your `DoublyLinkedList<T>` in a main method belonging to the same class.
There's no need to test your `DoublyLinearNode<T>`.




# Homework 6, Part B: Implement a Queue






<br/>

# Submission Checklist

* You submitted **all** `.java` files and all `.txt` files.
* Your files are named **exactly** as in the homework specification, *including file extensions*.
* You tested **every possible** pathway in your code.
* You signed every class (or file) with `@author` and `@version`, accompanied by a description of what the class does.
* You wrote javadoc for every function, which includes `@param` and `@return`.
* You wrote inline comments explaining the logic of your code.





<!--


# Homework 6: Stacks and Linked Lists


## Learning Goals

* Gaining experience with using multiple implementations for the same task
* Work with [Java's Stack class](https://docs.oracle.com/javase/8/docs/api/java/util/Stack.html)
* Work with [Java's LinkedList class](https://docs.oracle.com/javase/8/docs/api/java/util/LinkedList.html)
* Think about time complexity and compare different programs based on it

## Three ways to store a collection

### Task 1: CDcollection using a Stack and a LinkedList

Recall the very first collection we saw in this class, the `CDcollection`. It uses an array to keep track of the `CD`s in someone's possession. A client program, `Tunes`, acts as a driver for the `CDcollection`. In this exercise you will write two more implementations for managing a collection of CDs:
  1. `CDcollection_Stack`, which will use a Stack to manage the collection, and
  2. `CDcollection_LinkedList` which will use a LinkedList to do so.

Create a BlueJ project, adding the three files below to it. Review the code to refresh your memory on how the application works.

`CD.java`:
```java
//********************************************************************
//  CD.java       Java Foundations
//
//  Represents a compact disc.
//********************************************************************

import java.text.NumberFormat;

public class CD
{
   private String title, artist;
   private double cost;
   private int tracks;

   //-----------------------------------------------------------------
   //  Creates a new CD with the specified information.
   //-----------------------------------------------------------------
   public CD (String name, String singer, double price, int numTracks)
   {
      title = name;
      artist = singer;
      cost = price;
      tracks = numTracks;
   }

   //-----------------------------------------------------------------
   //  Returns a string description of this CD.
   //-----------------------------------------------------------------
   public String toString()
   {
      NumberFormat fmt = NumberFormat.getCurrencyInstance();

      String description;

      description = fmt.format(cost) + "\t" + tracks + "\t";
      description += title + "\t" + artist;

      return description;
   }
}
```

`CDCollection.java`:
```java
//********************************************************************
//  CDCollection.java       Java Foundations
//
//  Represents a collection of compact discs.
//********************************************************************

import java.text.NumberFormat;

public class CDCollection
{
   private CD[] collection;
   private int count;
   private double totalCost;

   //-----------------------------------------------------------------
   //  Constructor: Creates an initially empty collection.
   //-----------------------------------------------------------------
   public CDCollection ()
   {
      collection = new CD[100];
      count = 0;
      totalCost = 0.0;
   }

   //-----------------------------------------------------------------
   //  Adds a CD to the collection, increasing the size of the
   //  collection if necessary.
   //-----------------------------------------------------------------
   public void addCD (String title, String artist, double cost,
                      int tracks)
   {
      if (count == collection.length)
         increaseSize();

      collection[count] = new CD (title, artist, cost, tracks);
      totalCost += cost;
      count++;
   }

   //-----------------------------------------------------------------
   //  Returns a report describing the CD collection.
   //-----------------------------------------------------------------
   public String toString()
   {
      NumberFormat fmt = NumberFormat.getCurrencyInstance();

      String report = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n";
      report += "My CD Collection\n\n";

      report += "Number of CDs: " + count + "\n";
      report += "Total cost: " + fmt.format(totalCost) + "\n";
      report += "Average cost: " + fmt.format(totalCost/count);

      report += "\n\nCD List:\n\n";

      for (int cd = 0; cd < count; cd++)
         report += collection[cd].toString() + "\n";

      return report;
   }

   //-----------------------------------------------------------------
   //  Increases the capacity of the collection by creating a
   //  larger array and copying the existing collection into it.
   //-----------------------------------------------------------------
   private void increaseSize ()
   {
      CD[] temp = new CD[collection.length * 2];

      for (int cd = 0; cd < collection.length; cd++)
         temp[cd] = collection[cd];

      collection = temp;
   }
}
```

`Tunes.java`:
```java
//********************************************************************
//  Tunes.java       Java Foundations
//
//  Demonstrates the use of an array of objects.
//********************************************************************

public class Tunes
{
   //-----------------------------------------------------------------
   //  Creates a CDCollection object and adds some CDs to it. Prints
   //  reports on the status of the collection.
   //-----------------------------------------------------------------
   public static void main (String[] args)
   {
      CDCollection music = new CDCollection ();

      music.addCD ("Storm Front", "Billy Joel", 14.95, 10);
      music.addCD ("Come On Over", "Shania Twain", 14.95, 16);
      music.addCD ("Soundtrack", "Les Miserables", 17.95, 33);
      music.addCD ("Graceland", "Paul Simon", 13.90, 11);

      System.out.println (music);

      music.addCD ("Double Live", "Garth Brooks", 19.99, 26);
      music.addCD ("Greatest Hits", "Jimmy Buffet", 15.95, 13);

      System.out.println (music);
   }
}
```


**Task 1A: Prepare the Client program** (Tunes class)

Prepare the client program `Tunes` first. The client should create the same collection of CDs:
first using the array implementation of the CD collection, (as it currently is), then using the `CDcollection_Stack`, and finally using `CDcollection_LinkedList`.

When this client program executes, the output should be presented so that it is clear which part of it is produced by which implementation.

**Task 1B: CD collection using a Stack** (CDcollection_Stack class)

Define the `CDcollection_Stack` class. As said already, you have to employ a Stack to hold the CDs. Use [java's Stack class](https://docs.oracle.com/javase/8/docs/api/java/util/Stack.html) for it. (Think about: What other Stack implementations could you have used?)

Define any methods you need in order to have a well-designed Object Oriented Program. The goal is  that the client produces output identical to the original output of `Tunes`.

Run your program and compare its output with the original one.

**Task 1C: CD collection using a LinkedList** (CDcollection_LinkedList class)

Similar to the previous task, define the `CDcollection_LinkedList` class. This time the CDs will be held in a LinkedList. Use [java's LinkedList](https://docs.oracle.com/javase/8/docs/api/java/util/LinkedList.html) implementation. (Think about: What other LinkedList implementations could you have used?)

Once more, the output from the client should be identical to the two previous ones. Your client should print the very same thing three times, each time using a different implementation.

### Task 2: Complexity of the three implementations
At this point you have three different implementations for the same task: to manage a (very simple) collection of CDs.

You might be wondering "why do we need three programs all doing exactly the same thing?"

One reason might be **time complexity**: different implementations may have different running times. Then a client -depending on their specific circumstances- may choose one over another.

In a couple of paragraphs compare these three implementations. What are the pros and cons of each one? Write your thoughts in a file named `Complexity.txt`.

In another paragraph, describe what you learned from this exercise.

### How to submit your Work
Submit `Tunes.java`, `CDcollection_Stack.java`, `CDcollection_LinkedList.java` and  the `Complexity.txt` to Gradescope. You do not need to submit any prinout of the client. Don't forget to test **each one** of these Java classes.

And as always, add appropriate javadoc, including `@author` and `@version` tags!




<br/>

# Submission Checklist

* You submitted **all** `.java` files and all `.txt` files.
* Your files are named **exactly** as in the homework specification, *including file extensions*.
* You tested **every possible** pathway in your code.
* You signed every class (or file) with `@author` and `@version`, accompanied by a description of what the class does.
* You wrote javadoc for every function, which includes `@param` and `@return`.
* You wrote inline comments explaining the logic of your code.


-->