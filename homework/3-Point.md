## Goals

* Define and use your first Java classes
<!-- * Understand better the difference between static and instance methods -->
<!-- Refresh your memory on how to use recursion -->
* Understand how to compare floats

## Task:  Points and Distances

### Point Class
Create a class, named <code>Point</code> to represent a point on the Cartesian plane.
[Study our own Point documentation.](assign201/doc/Point.html)

### Step 1: Instance variables
 A point in the Cartesian plane has **x** and **y** coordinates, both of type `double`.

### Step 2: Constructors
Provide two constructors:
* A constructor without parameters creates a Point at location (0.0, 0.0).
* A two-parameter constructor takes as input two double numbers corresponding to x and y, and constructs an object of type Point at location (x,y).

### Step 3: toString()
As with any other class you write, define a **toString()** method to provide the means of
printing the contents of the object in an informative and concise way.

### Step 4: Getters and setters
Include appropriate getters and setters. Make sure to check the [javadoc](assign201/doc/Point.html) to see which getters and setters we expect.

### Step 5: Instance methods

Define the following instance methods:

* **findDistance()**: an *instance* method that takes as parameter a `Point`. It computes and returns the distance between the current `Point` (also known as <code>this</code>) and the parameter, using the Pythagorean formula.

* **areEquidistant()**: an *instance* predicate method that takes as input two `Point` objects, and returns true iff (if and only if) the distances between the current (`this`) Point and each of the input points differ by less than some amount called *TOLERANCE*. Define TOLERANCE as a final variable with the value of 0.01.

<!--* **readPoint()**: a *static* method that reads the **x** and **y** coordinates from the keyboard, and calls the constructor to create and return a new `Point` object.-->

* Include a  **main()** method for testing purposes. Make sure to create at least three instances of type `Point`. Compute, and report if any of the points created is equidistant to the other two.


### Notes and tips:

* Read the book section about comparing floating point values. It is recommended that you do not use "==". Tip: The *TOLERANCE* will be helpful here.  
* The `main` method should be short and high level: It should consist primarily of calling other methods from the class.
* Make sure to test each method carefully before moving on to the next one.
* Choose your testing cases carefully to thoroughly test all the methods you defined. Print what you expect the test to produce and the result of your method call.
* When finished, save the printout of your `main` into a file named <code>TestingPoint.txt</code>. You will submit this file too.
* Make sure to read the javadoc provided carefully, to ensure your methods work as expected.

<!--* We recommend that you implement and test the *instance* methods first, and leave the static *readPoint()* for last. We encourage you to test the instance methods using "hard values" first, like for example: `new Point(1.0, 2.0)`. This way you can test your code in a quick and efficient way. Using the *readPoint()* to get the input from every single testing from the keyboard would be very time consuming.
Of course, once you have the *readPoint()* defined, you will need to test it appropriately.-->
## What to submit:

* Submit only your <code>Point.java</code> file and a <code>TestingPoint.txt</code> file that contains the results of your testing.
* We expect your code to have careful and meaningful documentation on every method and for the whole file. Also, do not forget to include the `@author` and `@version` fields in the file documentation. Without them, the graders will not grade your work.

### Happy coding your first class!
