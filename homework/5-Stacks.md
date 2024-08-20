## Learning goals
* Get familiarity with Stacks
* Get familiarity with the package javafoundations
* Get experience with using Stacks with various implementations

## Task: Palindrome Checker using your preferred Stack implementation

A **palindrome** is a linear collection of objects that appear to be
in the same order when you list them in either direction (first to
last or last to first). In this task our palindromes will be strings.

* For example, String `madam` is a palindrome of characters that reads
the same forwards as backwards.
* So is `niconanomimatamimonanocin`
(meaning: "wash your sins, not only your face").

Write a program `PalindromeChecker.java` that uses 1 or 2 stacks to
determine if a string is a palindrome. You may want to use
`String.toCharArray` in putting characters onto a stack.

Think about your algorithm. Draw it. Take a picture and scan it. You
will submit this at the end.  Make sure to include all relevant
information in this representation, so that a reader who is only
familiar with the Stack interface understands your approach.

###Specifications

* Your program should contain a **predicate** method `isPalindrome()` that returns true or false as appropriate.

* Your main() method should use your preferred Stack implementation
  (we've studied two in class so far). Use print statements in main()
  to show that your method works correctly.

* You can only use the `toCharArray()` method in the String class to
  convert the input string in an array of characters from which you
  will populate a stack. **You cannot not use any other String methods
  or array operations, other than indexing into an array.**

* An input string is read as a `command-line argument` and is checked
  for the palindrome property. If there is no `args[0]` your program
  prints a message and continues execution (it does not crash). That
  way you can assign other strings as input and check for palindrome
  without having to re-run the program.

* Assume that the input string contains no spaces or special characters.

You are expected to **create your own test cases**, and demonstrate
that your code meets expectations. Remember that thorough testing
implies identifying and testing boundary cases as well.

## What to submit

Submit 3 files: your `PalindromeChecker.java` file, the picture
describing your strategy in using stacks, and your testing `.txt`
file.

## Optional Tasks

Do you want to do a little more programming for fun?
Try these:
* You could use the Java's Stack class.
* Create a JUnit testing file to test your design.
* Describe at least 2 different ways of using two stacks to solve the problem. Which one is better? Why?
