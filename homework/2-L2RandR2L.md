## Text reading the same in both directions

### Goals:
1. to work with Java's [Strings](https://docs.oracle.com/javase/7/docs/api/java/lang/String.html).
2. to practice method definitions and method invocations
3. to practice with extensive and appropriate testing
3. to practice with loops

### Task: L2R and R2L
#### Step 1: Study the problem
As you know, in order to understand a piece of text in a human language you need to read it either left-to-right (L2R), like in Anglophone languages, or right-to-left (R2L), like in Hebrew or Arabic. However, there are pieces of text that read exactly the same R2L and L2R, in the same language! Such texts are `dad` and `madamiamadam` in English, and  `νιψονανομηματαμημονανοψιν` ("wash your sins, not only your face") in Greek. Note that we only use lower case letters and no spaces.

In this problem you are asked to write a program to decide whether a given String holds the property of reading the same from L2R and R2L, and report the result:

* Yes, if the string holds the property, and

* No in the opposite case.


####  Step 2: The plan
As is the case with any non-trivial problem, there are more than ways to solve it. We encourage you to try to think of one on your own.

However, for this task, you need to implement the plan described here:
 * Write a method `reverseString()` that returns a copy of the input string containing its characters in reverse order.
 * Write a predicate method `theSame()` that compares two input strings (the original and the reversed copy) character-by-character. If all characters match, then it returns true. If not, it returns false.

Work the above strategy through a couple of examples and make sure you understand it before continuing.

####  Step 3: Write pseudocode
At this point you are ready to  express the strategy of solving this problem in pseudocode. Write it in your notebook, and take a picture of it. You will submit it at the end, together with the other files. Or, if you are using an electronic device to write, save your work in a file to submit at the end.

####  Step 4: Hand-execute the pseudocode
Run the produced pseudocode by hand on your examples. If you discover errors in the logic, fix them and repeat this step.

####  Step 5: Time to code!
Only now you are ready to start writing Java code.

Create a new project and add a class named `FunWithStrings`. In there:

1. Add a `main()` method to hold your testing as you go. The main() is the only static method in your program, the rest should not be. This means that you should create and use a dummy object:
<code>
FunWithStrings f = new FunWithStrings();
</code>

2. Define a fruitful method `reverseString()` that takes as input a string and returns another string with its characters in reverse order. Test this method to make sure it works as intended before moving to the next one.

3. Define a predicate method `theSame()` that takes two String inputs and checks whether they contain identical characters, one by one. If and only if the two strings are the same, the method should return true.
**Do not use the `equals() neither the compareTo()` methods from the String class here.**

4. Write the (top level) predicate method `sameBackAndForth()` that takes as input a string and determines whether it reads the same L2R and R2L.

5. Choose the testing cases thoughtfully. Use testing strings of various lengths (like 0, 1, 2, 3 and a longer one). Some of the testing strings should read the same in both directions, others not.

It is expected that your code has careful and meaningful **documentation** (top of the file and top of methods javadoc, as well as inline documentation). Top of the file javadoc should include values for the `@author` and `@version` tags. Top of the method javadoc should include values for the `@param` and `@return` tags as needed.

In BlueJ produce the `TestingL2RnR2L.txt` file to contain testing results from running the top level method (`sameBackAndForth()`). (Terminal Window --> Options --> Save to file...)


Testing results should include both expected and computed outcome, like : `input: dad. Expect: true Computed: true`.

### Submission:
1. Submit the following files (only):
   * `PseudocodeL2RnR2L` (with the appropriate file extension) containing your pseudocode
   * `FunWithStrings.java` containing your java code
   * `TestingL2RnR2L.txt` containing your test results


###(OPTIONAL) Do you want to check that your code passes our basic tests?

Use the [FunWithStringsTest.java](https://cs.wellesley.edu/~cs230/assignments/assign107/FunWithStringsTest.java) code we provide here.
