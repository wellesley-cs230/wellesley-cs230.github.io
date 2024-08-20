## Goals:
Practice with:
* working with BlueJ IDE to write, compile, run simple java programs
* java primitive data types, expressions and operators
* reading from the standard input (Scanner)
* practicing loops
* selecting testing values


## Exercise: Fun-Fun-Fun with loops

###Description###
In this exercise, you will learn how to use different types of loops in your code, based on the needs of that program. You are given [the starter code](assign103/Funloops.java), and your goal is to fill in the body of the empty methods with logic based on the descriptions below.

**Part1: The parrot**
Complete the method `parrot()` in the starter code provided for you. This method will keep prompting the user to enter a number that is greater than 0. Each time the user enters a number that is greater than 0, the method will print it out, and prompt the user to enter another number. This mimicking will stop only if the user enters the number 0.

**Part2: The toddler**
Complete the method `toddler()` in the starter code provided for you. This method will be given a number as parameter and it will list out all numbers from 1 to that number.

**Part3: The dreamer**
Complete the method `dreamer()` in the starter code provided for you. This method will be given a number as parameter and then it will draw a right-angled triangle of stars. The height and base of that triangle will consist of a number of stars equal to the input number.

Please note:
* We recommend you start by writing on a piece of paper how the three methods should work. You need to know what your correct answer should look like before you program!
* You can assume that the user will enter valid input, in the form of integer numbers. You don't need to handle invalid inputs.
* The sample main() we have provided is not complete, in the sense that it does not show all the calls to the methods. To test them you should call each one multiple times. 
* You should test each method you implemented above separately. They should not depend on each other.
* Some methods can be implemented using more than one type of loop. We will accept all correct answers, as long as the code is not overly complicated.


### Testing your program###

Think carefully about the set of inputs (testing cases) you will provide to your program to assert its correctness. Your inputs should be such that every method you wrote is tested (invoked) as your program runs.

In BlueJ, save the results of your testing produced in the "BlueJ: Terminal Window" into a file called loopsTest.txt. (Options > Save to File...)

### What to submit###

It is a standard policy of this course that submissions that have not been signed (`@author`) and dated (`@version`) will not be graded.

Your Gradescope submission should contain the following:

1. your <code>Funloops.java</code> source file
2. your <code>loopsTest.txt</code> text file that contains your testing results
