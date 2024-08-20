### Learning Goals

* Gaining experience with using multiple implementations for the same task
* Work with Java's Stack class
* Work with Java's LinkedList class
* Think about time complexity and compare different programs based on it

## Three ways to store a collection

### Task 1: CDcollection using a Stack and a LinkedList

Recall the very first collection we saw in this class, the `CDcollection`. It uses an array to keep track of the `CD`s in someone's possession. A client program, `Tunes`, acts as a driver for the `CDcollection`.

Download these three files (`CD.java`, `CDcollection.java` and `Tunes.java`) from the course material linked from the schedule.

Create a BlueJ project. Add these three source files to it. Review the code  carefully to refresh your memory on how the application works.

In this exercise you will write two more implementations for managing a collection of CDs:
  1. `CDcollection_Stack`, which will use a Stack to manage the collection, and
  2. `CDcollection_LinkedList` which will use a LinkedList to do so.

**Task 1A: Prepare the Client program** (Tunes class)

Prepare the client program `Tunes` first. The client should create the same collection of CDs:
first using the array implementation of the CD collection, (as it currently is), then using the `CDcollection_Stack`, and finally using `CDcollection_LinkedList`.

When this client program executes, the output should be presented so that it is clear which part of it is produced by which implementation.

 **Task 1B: CD collection using a Stack** (CDcollection_Stack class)

Define the `CDcollection_Stack` class. As said already, you have to employ a Stack to hold the CDs. Use java's Stack class for it. (Think about: What other Stack implementations could you have used?)

Define any methods you need in order to have a well-designed Object Oriented Program. The goal is  that the client produces output identical to the original output of `Tunes`.

Run your program and compare its output with the original one.

**Task 1C: CD collection using a LinkedList** (CDcollection_LinkedList class)

Similar to the previous task, define the `CDcollection_LinkedList` class. This time the CDs will be held in a LinkedList. Use java's LinkedList implementation. (Think about: What other LinkedList implementations could you have used?)

Once more, the output from the client should be identical to the two previous ones. Your client should print the very same thing three times, each time using a different implementation.

### Task 2: Complexity of the three implementations
At this point you have three different implementations for the same task: to manage a (very simple) collection of CDs.

You might be wondering "why do we need three programs all doing exactly the same thing?"

One reason might be **time complexity**: different implementations may have different running times. Then a client -depending on their specific circumstances- may choose one over another.

In a couple of paragraphs compare these three implementations. What are the pros and cons of each one? Write your thoughts in a file named `Complexity.txt`.

In another paragraph, describe what you learned from this exercise.

### How to submit your Work
Submit the `CDcollection_Stack.java`, `CDcollection_LinkedList.java` and  the `Complexity.txt` to Gradescope. You do not need to submit any prinout of the client.

And as always, add appropriate javadoc, including @author and @version tags!

**Good luck!**
