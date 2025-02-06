---
layout: default
---

# Homework 3, Part A: Flights


## Learning Goals
* Define and use your own proper Java classes
* Work with both static and instance methods
* Continue thinking about and writing testing code
* Practice with writing good and useful documentation

## Task: Flights and Stopovers <small>Flight Class</small>

Implement a class called `Flight`, following its specification in [its javadoc](/docs/Flight.html).

### Step 1: Instance variables
You'll notice from the javadoc, a `Flight` has several properties, including:
1. the name of the airline,
2. the flight number,
3. the flight's origin city, and
4. the flights's destination city.

### Step 2: Constructor
Create a constructor for a `Flight` object. This should take as input all the needed information to create a flight. How many parameters should it have? What types should these parameters be?

### Step 3: Instance and static methods

Implement the `Flight` class's method from the javadoc. Among them are the following **instance** methods:

1. `toString`. As with any other class you write, define this method to provide the means of printing the contents of the object in an informative and concise way. Don't forget to use this method as you test your code in the main.
2. `isAnAlternative`, a predicate method that takes as input a flight and returns true iff (if and only if) the invoker flight's origin and destination are the same as the input flight's origin and destination.
3. `isAStopOver`, a predicate method that takes as input a flight and returns true iff (if and only if) the invoker flight's destination is the same as the input flight's origin.

Additionally, implement the **static** methods, including:
1. `readFlight`, a *static* method that asks and collects from the user all the information regarding a flight. Using this information, it creates a `Flight`, and returns it. This method takes as input a `Scanner`.
2. Make sure to include a  `main` method, for testing purposes. As always, make sure you test all the methods you have defined, and to test each method before moving onto the next one.


### Step 4: Testing

It is important that you write code in your `main` method to test your program thoroughly. In it, create a few `Flight` objects, and test all your methods on them. Save the results of your testing into `FlightTesting.txt` to be submitted with your source code. You can take a look at the result of our test code for inspiration:


```text
Testing manual entry
New Flight f1 entered:AA123 from BOS to LAX 

Testing constructor
New Flight f2 created:DL55 from LAX to SFO 

Testing constructor
New Flight f3 created:OA1234 from SFO to ATH 

Testing getAirline(f1):(AA)->: AA

Testing getFlightNumber(f1):(123)->: 123

Testing getOrigin(f1):(BOS)->: BOS

Testing getDestination(f1):(LAX)->: LAX

Flights AA123 from BOS to LAX  and DL55 from LAX to SFO  share stopover city (TRUE)->: true

Flights DL55 from LAX to SFO  and AA123 from BOS to LAX  share stopover city (FALS)->: false

Flights DL55 from LAX to SFO  and OA1234 from SFO to ATH  share stopover city (TRUE->): true

Testing setDestination(f1):BOS

Testing setOrigin(f1):SFO

Testing changes to Flight f1:AA123 from SFO to BOS
 
Flights AA123 from SFO to BOS  and DL55 from LAX to SFO  share stopover city (FALSE)->: false

Flights DL55 from LAX to SFO  and AA123 from SFO to BOS  share stopover city (TRUE)->: true
```


### Step 5: Unit-Testing your code (optional, but recommended!)

Use the code below to test your implementation. To do this, create a new class, `FlightTest.java`, and replace its content with the code below. After compiling all of your code, write click on the class in the project viewer, and select "Test All." You will be using this code in the next homework, so it's good to make sure it's correct!


`FlightTest.java`:
```java
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.Assert;

/**
 * The test class FlightTest.
 *
 * @author  TM
 * @version 2022.09.23
 */
public class FlightTest
{
    private Flight f1, f2, f3;
    
    /**
     * Default constructor for test class FlightTest
     */
    public FlightTest()
    {

    }

    /**
     * Sets up the test fixture.
     *
     * Called before every test case method.
     */
    @BeforeEach
    public void setUp()
    {
        f1 = new Flight("AA", 123, "BOS", "LAX");
        f2 = new Flight("DL", 55, "LAX", "SFO");
        f3 = new Flight("OA", 1234, "SFO", "ATH");

    }

    /**
     * Tears down the test fixture.
     *
     * Called after every test case method.
     */
    @AfterEach
    public void tearDown()
    {
    }
    
    @Test
    public void testConstructor(){
        assertEquals(f1.getAirline(), "AA");
        assertEquals(f1.getFlightNumber(), 123);
        assertEquals(f1.getOrigin(), "BOS");
        assertEquals("LAX", f1.getDestination());
    }

    @Test
    public void testGetAirline(){
        assertEquals(f1.getAirline(), "AA");
        assertEquals(f2.getAirline(), "DL");
        assertEquals(f3.getAirline(), "OA");
    }

    @Test
    public void testGetOrigin()
    {
        assertEquals(f1.getOrigin(), "BOS");
        assertEquals(f2.getOrigin(), "LAX");
        assertEquals(f3.getOrigin(), "SFO");
    }
    
    @Test
    public void testStopOver()
    {
        assertEquals(f1.isAStopOver(f2),true);
        assertEquals(f2.isAStopOver(f1),false);
        assertEquals(f2.isAStopOver(f3),true);
    }
    
    @Test
    public void testSetOrigin(){
        f1.setOrigin("SFO");
        assertEquals(f1.getOrigin(), "SFO");
        assertEquals(f1.isAStopOver(f2),true);
        assertEquals(f2.isAStopOver(f1),true);
    }
    

    @Test
    public void testGetDestination()
    {
        assertEquals("LAX", f1.getDestination());
        assertEquals("SFO", f2.getDestination());
        assertEquals("ATH", f3.getDestination());
    }
}
```



## What to submit
* Submit only your `Flight.java` and your `FlightTesting.txt` that contains the results of your testing.
* We expect your code to have careful and meaningful documentation (inline as well as Javadoc) on every method and for the whole file. Also, do not forget to include the `@author` and `@version` fields in the file documentation.






<br/>


# Homework 3, Part B: Point


## Goals

* Define and use your first Java classes
<!-- * Understand better the difference between static and instance methods -->
<!-- Refresh your memory on how to use recursion -->
* Understand how to compare floats


## Task:  Points and Distances


Create a class, named `Point` to represent a point on the Cartesian plane, following [this javadoc](/docs/Point.html).


### Step 1: Instance Variables
 A point in the Cartesian plane has **x** and **y** coordinates, both of type `double`.

### Step 2: Constructors
Provide two constructors:
* A constructor without parameters creates a `Point` at location (0.0, 0.0).
* A two-parameter constructor takes as input two `double` numbers corresponding to x and y, and constructs an object of type `Point` at location (x, y).

### Step 3: `toString`
As with any other class you write, define a `toString` method to provide the means of
printing the contents of the object in an informative and concise way.

### Step 4: Getters and Setters
Include appropriate getters and setters. Make sure to check the [javadoc](/docs/Point.html) to see which getters and setters we expect.

### Step 5: Instance Methods

Define all instance methods listed in the javadoc, including:
* `findDistance`: an *instance* method that takes as parameter a `Point`. It computes and returns the distance between the current `Point` (also known as `this`) and the parameter, using the Pythagorean formula.
* `areEquidistant`: an *instance* predicate method that takes as input two `Point` objects, and returns true iff (if and only if) the distances between the current (`this`) Point and each of the input points differ by less than some amount called *TOLERANCE*. Define TOLERANCE as a final variable with the value of 0.01.
* `readPoint`: a *static* method that reads the **x** and **y** coordinates from the keyboard, and calls the constructor to create and return a new `Point` object.
* Include a  `main` method for testing purposes. Make sure to create at least three instances of type `Point`. Compute, and report if any of the points created is equidistant to the other two.


### Notes and Tips:

* Read the book section about comparing floating point values. It is recommended that you do not use `==`. Tip: The *TOLERANCE* will be helpful here.  
* The `main` method should be short and high level: It should consist primarily of calling other methods from the class.
* Make sure to test each method carefully before moving on to the next one.
* Choose your testing cases carefully to thoroughly test all the methods you defined. Print what you expect the test to produce and the result of your method call.
* When finished, save the printout of your `main` into a file named `TestingPoint.txt`. You will submit this file too.
* Make sure to read the javadoc provided carefully, to ensure your methods work as expected.
* We recommend that you implement and test the *instance* methods first, and leave the static *readPoint* for last. We encourage you to test the instance methods using "hard values" first, like for example: `new Point(1.0, 2.0)`. This way you can test your code in a quick and efficient way. Using the *readPoint* to get the input from every single testing from the keyboard would be very time consuming.
Of course, once you have the *readPoint* defined, you will need to test it appropriately.

## What to submit:

* Submit only your `Point.java` file and a `TestingPoint.txt` file that contains the results of your testing.
* We expect your code to have careful and meaningful documentation on every method and for the whole file. Also, do not forget to include the `@author` and `@version` fields in the file documentation. Without them, the graders will not grade your work.



<br/>

# Submission Checklist

* You submitted **all** `.java` files and all `.txt` files.
* Your files are named **exactly** as in the homework specification, *including file extensions*.
* You tested **every possible** pathway in your code.
* You signed every class (or file) with `@author` and `@version`, accompanied by a description of what the class does.
* You wrote javadoc for every function, which includes `@param` and `@return`.
* You wrote inline comments explaining the logic of your code.
* You added getters and setters where it makes sense to have them (i.e. with good encapsulation practices)

