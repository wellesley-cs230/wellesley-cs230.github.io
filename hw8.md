---
layout: default
---

# Homework 8: Who dunn it?!

**Goals:**
* Learn how to implement HashTables
* Learn two strategies for handling hash collisions
* Continue practicing the OOP paradigm


**Pair Programming:**
We will assign you a peer to collaborate with on this assignment. Please,
* Reach out to your partner ASAP to discuss when you will meet to work on the assignment. You will probably have to meet several times.
* Work *together* (pair programming) rather than splitting the homework and working separately.
* *Discuss* the ideas and diagrams before diving into coding.


**Context:** In the fall of 2024, Professors Yacoby and Sandu, embarked on an epic, never-ending saga of rivalry with the world's most cunning nemesis: the west-wing scanner. It all began when it gleefully devoured the students' CS 230 midterms and spewed forth an artistic masterpiece that looked more like a 3D Rorschach tests. Thankfully, Professor Sohie Lee was around to help us turn things around. Watching her work her magic, we learned that the scanner only responds well to scented candles, words of affirmation, and lots (and lots) of encouragement. But what caused the scanner to behave like this?

Enter Professor Turbak, whose tenure in the department dates back to the early 1900s—or so the legend goes. He reminisced about a chilly winter evening in 1982, when the scanner apparently committed "unspeakable things" that still induce dramatic pauses today. His theory? The scanner was hacked!

In an effort to unravel the mystery, we enlisted the expertise of Professors Scott Anderson and Alexa VanHattum, who helped us snag the scanner's logs, chronicling every IP address that dared whisper sweet nothings into its circuits. However, we were so traumatized by the scanner's antics that we seemed to have forgotten how to implement all data structures. Now, we desperately need your help.

If the scanner logs from 1982 reveal the same IP address as that fateful night when the midterms turned into modern art, it means our dear scanner wasn't just hacked---it was haunted by the same techno-ghost! Dust off your detective hats, because this is one glitch in the matrix you won't want to miss. Your mission, should you choose to accept it, is to determine if the same IP address was found in both logs.



<br/>

# Task 0

Create a new BlueJ project called "HashTables." In this project, create a file for the following interface:

`HashTable.java`:
```java
public interface HashTable<K, V> {
    /**
     * Inserts the specified key-value pair into the hash table. 
     * If the key already exists in the hash table, its value is updated to the specified value.
     *
     * @param key   The key with which the specified value is to be associated.
     * @param value The value to be associated with the specified key.
     */
    public void put(K key, V value);

    /**
     * Returns the value associated with the specified key, or null if the hash table contains no mapping for the key.
     *
     * @param key The key whose associated value is to be returned.
     * @return The value associated with the specified key, or null if the hash table contains no mapping for the key.
     */
    public V get(K key);

    /**
     * Returns the number of key-value mappings in the hash table.
     *
     * @return The number of key-value mappings in the hash table.
     */
    public int size();

    /**
     * Returns true if the hash table contains no key-value mappings.
     *
     * @return true if the hash table contains no key-value mappings.
     */
    public boolean isEmpty();
}
```

You will create several Hash Tables that implement this interface. Next, create a file called `Entry.java`, representing a single HashTable entry as follows. This will prove useful in your implementation of the Hash Tables.

`Entry.java`:
```java
/**
 * Represents an entry in the HashTable
 *
 * @author CS 230 Staff
 * @version Fall 2024
 */
public class Entry<K, V> {
    private K key;
    private V value;

    /**
     * Constructs an entry with the specified key and value.
     *
     * @param key   The key associated with this entry.
     * @param value The value associated with this key.
     */
    public Entry(K key, V value) {
        this.key = key;
        this.value = value;
    }

    /**
     * Returns the key associated with this entry.
     *
     * @return The key associated with this entry.
     */
    public K getKey() {
        return this.key;
    }

    /**
     * Sets the key for this entry.
     *
     * @param key The key to set for this entry.
     */
    public void setKey(K key) {
        this.key = key;
    }

    /**
     * Returns the value associated with this entry.
     *
     * @return The value associated with this entry.
     */
    public V getValue() {
        return this.value;
    }

    /**
     * Sets the value for this entry.
     *
     * @param value The value to set for this entry.
     */
    public void setValue(V value) {
        this.value = value;
    }

    /**
     * Determines whether the entries are equal, 
     * returning true if their keys equal.
     *
     * @param value The entry to compare with.
     */
    public boolean equals(Object obj) {
        Entry<K, V> other = (Entry<K, V>) obj;
        return this.key.equals(other.key);
    }
}
```

You will also need to read lines from the log files. Create a file called `FileIO.java` and copy the following code into it. You do not need to modify this class or explain how it works.

`FileIO.java`:
```java
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

/**
 * Provides a helper method for reading lines from files.
 *
 * @author CS 230 Staff
 * @version Fall 2024
 */
public class FileIO {
    /**
     * Reads all lines from a file.
     *
     * @param filename the name of the file to read
     * @return an array containing the lines in the file
     */
    public static String[] readLines(String filename) {
        try {
            Scanner input = new Scanner(new File(filename));

            int numberOfLines = 0;
            while (input.hasNextLine()) {
                numberOfLines++;
                input.nextLine();
            }
            input.close();

            input = new Scanner(new File(filename));
            String[] lines = new String[numberOfLines];

            for (int i = 0; i < lines.length; i++) {
                lines[i] = input.nextLine();
            }

            input.close();
            return lines;
        }
        catch (FileNotFoundException e) {
            System.out.println("Could not find file: " + filename);
            return new String[0];
        }
    }
}
```

For example, to read the lines from a file, use:

```java
String[] lines = FileIO.readLines("log-1982.txt");
```

<br/>

# Task 1

* Create a file called `LinearProbingHashTable.java` and in it, implement a HashTable with linear probing.
* Since all Java objects extend `Object`, they all inherit a method called `hashCode` that can be used in a hash table. In your HashTable, please use the `hashCode` method of `K` as your hash function. Note that this function may return a negative integer, so take the absolute value of the output of the function.
* At the bottom of the file, create a main method and use it to test your code. We recommend picking `K` to be a `String` when testing. Save the output of your tests in a file called `LinearProbingHashTable.txt` and submit it along with your code.



<br/>

# Task 2

* Create a file called `LinkedHashTable.java` and in it, implement a HashTable with separate chaining. For this class, you're welcome to use Java's `LinkedList` class.
* Add a method `public V remove(K key)` to this implementation that allows one to remove the item associated with the provided `key`. Note that this is not possible to do for a Hash Table with linear probing---can you think of why?
* As before, create a main method and use it to test your code and save the output of your testing in `LinkedHashTable.txt` to submit it along with your code.


<br/>

# Task 3

Now that you have your HashTable ready, you can start your investigation! Implement a driver class called `Detective.java` that:
* Reads in the log files from [1982](/static_files/hashtables/log-1982.txt) and [2024](/static_files/hashtables/log-2024.txt), containing the lists of IP addresses
* Uses one of your Hash Table implementations to cross references the IP addresses from 1982 with those from 2024 to find the overlap
* For the IP address that overlap, your code should report how many times the IP address appears in each log

Use the following code to read the log files:

```java
String[] log1982 = FileIO.readLines("log-1982.txt");
String[] log2024 = FileIO.readLines("log-2024.txt");
```

<br/>

# Task 4

In a file called `Answers.txt`, answer:
1. Which IP address did you find? Is it a valid IP address (you may use Google to help you answer this)? 
2. How many times did it appear in the 1982 log and in the 2024 log?
3. If the log from 1982 had `N` lines and the file from 2024 had `M` lines, what's the computational complexity of your algorithm?
4. And what's the space complexity of your algorithm?


<br/>

# Submission Checklist

* You submitted **all** `.java`, `.txt` and `.pdf` files.
* Your files are named **exactly** as in the homework specification, *including file extensions*.
* You tested **every possible** pathway in your code.
* You signed every class (or file) with `@author` and `@version`, accompanied by a description of what the class does.
* You wrote javadoc for every function, which includes `@param` and `@return`.
* You wrote inline comments explaining the logic of your code.