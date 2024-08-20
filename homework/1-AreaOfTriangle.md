## Goals:
Practice with:
* working with BlueJ IDE to write, compile, run simple java programs
* java primitive data types, expressions and operators
* reading from the standard input (Scanner)
* defining and calling methods
* understanding the complexities of number conversions
* selecting testing values


## Exercise: Area of a Triangle

###Description

Write a program, `AreaTriangle`, that prompts the user three times for the side
lengths of a triangle. Based on these three inputs, the program checks and prints whether this triangle is isosceles or not, as well as its area.
In addition to the `main()` method, **your program should also define three
other static methods** :
  1. a predicate method `isValidTriangle()` to check whether the three inputs define a triangle, based on the **triangular inequality** (that is, the sum of any two sides of a triangle is strictly greater than the third side),
  2. a method to `getHeronArea()` compute the triangle's area based on [Heron's Formula](http://en.wikipedia.org/wiki/Heron%27s_formula) given the three side lengths,
  3. a predicate method `isIsosceles()`  to check whether the triangle is isosceles

Some important notes on this exercise:

* Equilateral triangles are considered isosceles.
*  If the user enters three side lengths that cannot possibly form a triangle
   (ex. 1,1,2), your program should that this set of input does not form a triangle and stop execution. You can use `System.exit(1)` for that. 
* You do not need to handle the case when the user enters other invalid input, e.g. negative number(s) or non-numbers.

Some sample executions of this program are shown below:

<center><img src="figs/triangleExecution.png" style="max-width:900px"></center>

### Testing your program

Think carefully about the set of inputs (testing cases) you will provide to your program to assert its correctness. Your inputs should be such that every method you wrote is tested (invoked) as your program runs.

Make sure you give reasonable and useful names to your methods, and that you write meaningful comments in your program.

In BlueJ, save the results of your testing produced in the "BlueJ: Terminal Window" into a file called AreaTriangleTest.txt. (Options > Save to File...)

### What to submit

It is a standard policy of this course that submissions that have not been signed (`@author`) and dated (`@version`) will not be graded.



Your Gradescope submission should contain the following:

1. your <code>AreaTriangle.java</code> file
2. your <code>AreaTriangleTest.txt</code> file that contains your testing results
