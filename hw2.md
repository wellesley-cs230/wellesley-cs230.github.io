---
layout: default
---

# Homework 2, Part A: Fun with Strings

## Goals:
1. to work with Java's [Strings](https://docs.oracle.com/javase/7/docs/api/java/lang/String.html).
2. to practice method definitions and method invocations
3. to practice with extensive and appropriate testing
3. to practice with loops

## Task: L2R and R2L

### Step 1: Study the problem
As you know, in order to understand a piece of text in a human language you need to read it either left-to-right (L2R), like in Anglophone languages, or right-to-left (R2L), like in Hebrew or Arabic. However, there are pieces of text that read exactly the same R2L and L2R, in the same language! Such texts are `dad` and `madamiamadam` in English, and  `νιψονανομηματαμημονανοψιν` ("wash your sins, not only your face") in Greek. Note that we only use lower case letters and no spaces.

In this problem you are asked to write a program to decide whether a given String holds the property of reading the same from L2R and R2L, and report the result:

* Yes, if the string holds the property, and

* No in the opposite case.


###  Step 2: The plan
As is the case with any non-trivial problem, there are more than one way to solve it. We encourage you to try to think of one on your own.

However, for this task, you need to implement the plan described here:
 * Write a method `reverseString()` that returns a copy of the input string containing its characters in reverse order.
 * Write a predicate method `theSame()` that compares two input strings (the original and the reversed copy) character-by-character. If all characters match, then it returns true. If not, it returns false.

We recommend working through the above strategy a couple of examples and make sure you understand it before continuing.

###  Step 3: Write pseudocode
At this point you are ready to  express the strategy of solving this problem in pseudocode. Write it in your notebook, and take a picture of it. You will submit it at the end, together with the other files. Or, if you are using an electronic device to write, save your work in a file to submit at the end.

###  Step 4: Hand-execute the pseudocode
Run the produced pseudocode by hand on your examples. If you discover errors in the logic, fix them and repeat this step.

###  Step 5: Time to code!
Only now you are ready to start writing Java code.

Create a new project and add a class named `FunWithStrings`. In there:

1. Add a `main()` method to hold your testing as you go. 

2. Add method `public static String reverseString(String s)` that takes as input a string and returns another string with its characters in reverse order. Test this method to make sure it works as intended before moving to the next one.

3. Add a predicate method `public static boolean theSame(String s1, String s2)` that takes two String inputs and checks whether they contain identical characters, one by one. If and only if the two strings are the same, the method should return true. For the purposes of the exercise, **please do not use the `equals()` or the `compareTo()` methods from the String class here.**

4. Add a predicate method `public static boolean sameBackAndForth(String s)` that takes as input a string and determines whether it reads the same L2R and R2L.

5. Choose the testing cases thoughtfully. Use testing strings of various lengths (like 0, 1, 2, 3 and a longer one). Some of the testing strings should read the same in both directions, others not.

It is expected that your code has careful and meaningful **documentation** (top of the file and top of methods javadoc, as well as inline documentation). Top of the file javadoc should include values for the `@author` and `@version` tags. Top of the method javadoc should include values for the `@param` and `@return` tags as needed.

In BlueJ produce the `TestingL2RnR2L.txt` file to contain testing results from running the top level method (`sameBackAndForth()`). (Terminal Window --> Options --> Save to file...)


Testing results should include both expected and computed outcome, like: `input: dad. Expect: true Computed: true`.

## Submission:
1. Submit the following files (only):
   * `PseudocodeL2RnR2L` (with the appropriate file extension) containing your pseudocode
   * `FunWithStrings.java` containing your java code
   * `TestingL2RnR2L.txt` containing your test results


## Check if your code passes our basic tests (optional)

Use the code below to test your implementation. To do this, create a new class, `FunWithStringsTest.java`, and replace its content with the code below. After compiling all of your code, write click on the class in the project viewer, and select "Test All."

`FunWithStringsTest.java`:
```java 
import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;

public class FunWithStringsTest {

    @Before
    public void setUp() {
        // N/A
    }

    @Test
    public void testReverseString() {
        assertEquals("edcba", FunWithStrings.reverseString("abcde"));
        assertEquals("gfedcba", FunWithStrings.reverseString("abcdefg"));
        assertEquals("", FunWithStrings.reverseString(""));
        assertEquals("a", FunWithStrings.reverseString("a"));
    }

    @Test
    public void testTheSame() {
        assertTrue(FunWithStrings.theSame("abc", "abc"));
        assertFalse(FunWithStrings.theSame("abc", "abcd"));
        assertFalse(FunWithStrings.theSame("abc", "abC"));
        assertFalse(FunWithStrings.theSame("abc", "ab"));
    }

    @Test
    public void testSameBackAndForth() {
        assertTrue(FunWithStrings.sameBackAndForth("aba"));
        assertTrue(FunWithStrings.sameBackAndForth("abcba"));
        assertFalse(FunWithStrings.sameBackAndForth("abca"));
        assertFalse(FunWithStrings.sameBackAndForth("abcde"));
    }
}
```





<br/>

# Homework 2, Part B: More String Operations

## Goals:
1. to work with some of Java's built-in [String class](https://docs.oracle.com/javase/7/docs/api/java/lang/String.html) methods
2. to refresh your memory on recursion

## Task:

Create a new class named **StringOps** and include definitions for the following (static) methods:

* `public static String removeChar(String str, char ch)`. This method returns a string that is constructed from the input string **str**, with the first occurrence of the character **ch** removed from it. If the character **ch** is not contained in the input string **str**, then this method returns the original string. Examples:  
  * `removeChar("java", 'q')` returns `"java"`
  * `removeChar("java", 'a')` returns `"jva"`
* `public static boolean testAnagrams(String word1, String word2)`.  It determines whether the two input strings **word1** and **word2** are anagrams. Returns true if the two  input strings are anagrams, false otherwise. An **anagram** is defined as two words that have exactly the same letters, possibly in a different order. Examples:
  * `testAnagrams("melon", "lemon")` returns `true`
  * `testAnagrams("hello", "world")` returns `false`
  * `testAnagrams("hello", "hello")` returns `true` (since a word is an anagram of itself)
* `main()`. As usual, it will contain your testing code. Make sure your testing is comprehensive, and your testing printing is informative, like in the following line:
  * Calling `testAnagrams(melon, lemon)`. Expect TRUE. Got: true

Finally, save the results of your program into a textfile named `StringOpsTesting.txt`. You will need to submit this text file along with the source code.

**Note:**
* You can assume that your input is all lowercase.
* Both of the above methods have elegant solutions using recursion. We encourage you (but we do not require) to try to solve them with recursion.

## Submitting
When done, submit your <code>StringOps.java</code> along with the <code>StringOpsTesting.txt</code> that shows the results of your comprehensive testing. Please DO NOT submit any other file but these two.

 
 
 
