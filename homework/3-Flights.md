## Learning Goals
* Define and use your own proper Java classes
* Work with both static and instance methods
* Continue thinking about and writing testing code
* Practice with writing good and useful documentation

## Task: Flights and Stopovers <small>Flight Class</small>

Implement a class called **Flight**
[(here is the Flight javadoc)](assign202/doc/Flight.html)
to represents an airline flight.

### Step 1: Instance variables
The following properties represent a Flight object:
1. the name of the airline,
2. the flight number,
3. the flight's origin city, and
4. the flights's destination city.

### Step 2: Constructor
Create a constructor for a Flight object. This should take as input all the needed information to create a flight. Think carefully: how many parameters should it have? What types should these parameters be?

### Step 3: instance methods
1. **toString()**
As with any other class you write, define a **toString()** method to provide the means of printing the contents of the object in an informative and concise way. Don't forget to use this method as you test your code in the main().

2. **isAnAlternative()**
a predicate method that takes as input a flight and returns true iff (if and only if) the invoker flight's origin and destination are the same as the input flight's origin and destination.

3. **isAStopOver()**
a predicate method that takes as input a flight and returns true iff (if and only if) the invoker flight's destination is the same as the input flight's origin.


### Step 4: Static methods
Create the following methods:

1. **readFlight()**:
a *static* method that asks and collects from the user all the information regarding a flight. Using this information, it creates a Flight, and returns it. This method takes as input a `Scanner`.

2. Make sure to include a  **main()** method, for testing purposes. As always, make sure you test all the methods you have defined, and to test each method before moving onto the next one.

It is important that you write code in your <code>main()</code> method to test your program thoroughly. In it create a few Flight objects, and test all your methods on them. You can take a look at the result of [(this testing code)](assign202/FlightTesting.txt) for inspiration. Save the results of your testing into `FlightTesting.txt` to be submitted with your source code.

### Notes and tips:

Our experience shows that early-stage programmers make a few common mistakes that could be avoided with a more careful final reading of the specifications (i.e., the description of the assignment in our case). We thought of helping you in this careful reading by adding here a few items to review before submission:

* Did you name your class and constructor correctly?
* Did you provide getters and setters for all instance variables?
* Did you name the methods reasonably (or exactly as asked)?
* Did you test each and every method in the main with printing statements that describe what they do? (e.g. `Testing getOrigin. Expecting: BOS. Producing: BOS`).
* Did you write meaningful (not verbose) documentation above the class definition and above each method?
* Did you try to imitate javadoc directives (like using @author, @param, @return, as needed)?
* Did you save your printout and named it as expected?
* Did you upload the 2 files you were asked to, and did you check that they were uploaded correctly?

## What to submit
* Submit only your <code>Flight.java</code> and your <code>FlightTesting.txt</code> that contains the results of your testing.
* We expect your code to have careful and meaningful documentation (inline as well as Javadoc) on every method and for the whole file. Also, do not forget to include the @author and @version fields in the file documentation.
