---
layout: default
---

# Homework 9, Part A: Guitar



## Learning Goals

* Extend a known Data Structure (Queue), to create a new, special-purpose Data Structure (BoundedQueue)
* Use this special-purpose Data Structure in an simulation of a guitar playing music

## Exercise: While My Guitar Gently Weeps

In this exercise, you will learn how to simulate the plucking of a guitar string with the Karplus-Strong algorithm. Play the video below to see a visualization of the algorithm. If your browser won't play the video below, you can right-click on it and save it to your Desktop to play it from there.


<p><center>
<video controls="controls" width="760" height="220" name="Stairway to Heaven" src="_images/figs/StairwayToHeaven.mov"></video>
</center></p>

When a guitar string is plucked, the string vibrates and creates sound. The length of the string determines its fundamental frequency of vibration. We model a guitar string by sampling its displacement (a real number between -1/2 and +1/2) at N equally spaced points (in time), where N equals the sampling rate (44,100) divided by the fundamental frequency (rounding the quotient up to the nearest integer).

<!--
When a guitar string is plucked, the string vibrates and creates sound. These are some terms regarding the physics about how guitars make noise, and our simulation of it in this exercise:
* When a guitar string is at rest, it is at its **equilibrium position**.
* When a string is strummed, it vibrates oscillating from side to side. At any point, the distance of the string from its equilibrium position is called the **displacement** and it changes constantly. We will measure it as a real number between -1/2 and +1/2.
* The **sampling rate** indicates how many samples of the displacement we take in a second. In out simulation the sampling rate **(N)** will be 44,100 (samples per second).
* The **fundamental frequency** of the vibration is determined by the string length. We model a guitar string by dividing its displacement by the fundamental frequency (rounding the quotient up to the nearest integer). We will take N such samples per second.

 at **N** equally spaced points (in time), where **N** equals the **sampling rate** (44,100) divided by the fundamental frequency (rounding the quotient up to the nearest integer).
-->
<img src="_images/figs/guitar-samples.png" />

**Plucking the string.** The excitation of the string contains energy at any frequency. We simulate the excitation with <em>white noise</em>:
set each of the <em>N</em> displacements to a random real number between -1/2 and +1/2.

<img src="_images/figs/white-noise.png" />

**The resulting vibrations.** After the string is plucked, the string vibrates. The pluck causes a displacement which spreads wave-like over time. The Karplus-Strong algorithm simulates this vibration by maintaining a <em>bounded-queue</em> of the <em>N</em> samples: the algorithm repeatedly dequeues the first sample from the bounded queue and enqueues the average of the dequeued sample and the front sample in the queue, scaled by an <em>energy decay factor</em> of 0.994.

<img src="_images/figs/karplus-strong.png" />


### Task 0

Download this [starting code](static_files/Guitar.zip) that will allow you to complete the tasks below.


### Task 1

Write a **BoundedQueue.java** class that implements a **bounded queue ADT**. A bounded queue is a queue with a **maximum capacity**: no elements can be enqueued when the queue is full to its capacity. The BoundedQueue class should *inherit* from the `javafoundations.CircularArrayQueue` class, given in the starting code.

Your *BoundedQueue.java* file should contain implementations for the following methods:

  * A **constructor** that takes an integer argument, which is the capacity of the bounded queue
  * A predicate `isFull()` that indicates whether the bounded queue is at capacity or not
  * An `enqueue()` method that overrides the `javafoundations.CircularArrayQueue`'s `enqueue()` method so that it only enqueues an element if the queue is not at capacity.

You should not add any more **instance** methods to this class implementation. But, of course, you should be providing evidence of testing your implementation in the `main()`.

Make sure you test this class before continuing to the next task.

### Task 2

Write a `GuitarString` class that models a vibrating guitar string according to the following contract:

  * <code>public GuitarString(double frequency);</code>
  The **constructor** creates a guitar string of the given *frequency*, using a sampling rate of 44,100. It initializes a bounded queue of the desired capacity *N* (sampling rate divided by the *frequency*, rounded up to the nearest integer), and fills the bounded queue with *N* zeros to model a guitar string at rest.<br>

  * <code>public void pluck();</code>
  The **pluck()** method replaces the *N* samples in the bounded queue with *N* random values between -0.5 and +0.5:<br>

  * <code>public double sample();</code>
  The **sample()** method returns the value of the item at the front of the bounded queue:<br>

  * <code>public void tic();</code>
  The **tic()** method applies the Karplus-Strong algorithm, i.e., it deletes the sample at the front of the bounded queue and adds to the end of the bounded queue the average of the deleted sample and the sample at the front of the bounded queue, multiplied by the energy decay factor of 0.994:


### Task 3

Now you should be ready to test your code from the previous tasks. Compile and run the provided **GuitarHeroine** application. If you have successfully completed the previous tasks, then when you run the application, a window should appear as follows:

<img src="_images/figs/guitar-heroine.png" />

Now, you can make sweet music. By pressing any of the keys on your computer keyboard corresponding to the notes as illustrated in the piano keyboard image, you can simulate plucking a guitar string for that note (make sure that your computer's sound is not muted).

### What to submit
In Gradescope submit the following files:

1. The `BoundedQueue.java` file
2. Your testing transcript (`BoundedQueue.txt`) for BoundedQueue class
3. The `GuitarString.java` file







<br/>

# Homework 9, Part B: Tree Recursion

## Learning Goals

* Practice recursive tree algorithms


## Tasks

First, create a BlueJ project with the following starter code.

`BTNode.java`:
```java
import java.util.LinkedList;

public class BTNode<T> {
    protected T element;
    protected BTNode<T> left, right;

    public BTNode(T elmt) {
        element = elmt;
        left = right = null;
    }

    public T getElement() { 
        return element; 
    }

    public void setElement(T element)
    { this.element = element; }

    public BTNode<T> getLeft() { 
        return left; 
    }

    public void setLeft(BTNode<T> left) { 
        this.left = left; 
    }

    public BTNode<T> getRight() { 
        return right; 
    }

    public void setRight(BTNode<T> right) {
        this.right = right; 
    }

    public BTNode<T> find(T target) {
        BTNode<T> result = null;

        if (element.equals(target)) {
            result = this;
        } else {
            if (left != null)
                result = left.find(target);
            if (result == null && right != null)
                result = right.find(target);
        }

        return result;
    }

    public int count() {
        int result = 1;

        if (left != null)
            result = result + left.count();

        if (right != null)
            result = result + right.count();

        return result;
    }
```

`BSTNode.java`:
```java
public class BSTNode<T extends Comparable<T>> extends BTNode<T> {

    public BSTNode(T element) {
        super(element);
    }

    public void add(T item) {
        if (item.compareTo(element) < 0) {
            if (left == null)
                left = new BSTNode(item);
            else //  Add recursively 
                ((BSTNode) left).add(item);
        } else { //  item >= element, go right
            if (right == null)
                right = new BSTNode (item);
            else //  Add recursively 
                ((BSTNode) right).add (item);
        }
    }

    public BSTNode<T> find(T target) {
        if (target.compareTo(element) == 0)
            return this;
            
        // Since left and right are defined as BTNodes in the parent class,
        // we cast them to BSTNodes here so we can call compareTo
        BSTNode<T> l = (BSTNode<T>) left;
        BSTNode<T> r = (BSTNode<T>) right;
        
        if (target.compareTo(element) < 0 && l != null) {
            return l.find(target);
        }
            
        if (r != null) {
            return r.find(target);
        }
        
        return null;
    }
}
```


Next, implement the following instance methods:
1. Implement `public int countLeaves()` in the `BTNode` class. This method should return an integer counting the number of leaves in tree.
2. Implement `public int countNodesAtLevel(int level)` in the `BTNode` class. This method should return the number of nodes at a given *level* in the tree. In this method, we'll say that level 0 represents the root.
3. Implement `public LinkedList<T> collectOnlyChildren()` in the `BTNode` class. This method should return a list of all elements `T` that belong to nodes that have no siblings.
4. Implement `public boolean isValid()` in the `BSTNode` class. This method should return `true` if the tree is a valid binary search tree.


Please test your code as you go, putting your test in a driver class called `Driver.java`.



<br/>

# Submission Checklist

* You submitted **all** `.java` files and all `.txt` files.
* Your files are named **exactly** as in the homework specification, *including file extensions*.
* You tested **every possible** pathway in your code.
* You signed every class (or file) with `@author` and `@version`, accompanied by a description of what the class does.
* You wrote javadoc for every function, which includes `@param` and `@return`.
* You wrote inline comments explaining the logic of your code.




