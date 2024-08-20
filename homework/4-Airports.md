##Learning Goals
* Using arrays to hold and maintain collection of objects
* Using loops to process array elements


## Exercise:  Airports!

Create a class named <code>Airport</code> that keeps track of the flights that
use a certain airport, either as their origin or destination. 
<!--Consult the provided [Airport](assign205/doc/Airport.html) javadoc-generated documentation.-->

### Specifications

For this exercise you are **NOT allowed to use any of Java's Arrays class**. Just use arrays of Objects as we did in lectures.

**0. Draw your class objects as you design and before you code them.**
You will need to submit a picture of your drawing, so keep it (reasonably) neat and clean. If you need a reminder on how to draw these class objects, make sure to revisit the slides and see the CD and CDCollection objects. 

Your class should contain the following:

**1.  Instance variables**
  * the name of the Airport
  * an array to keep track of the Flights that use this airport (as its origin or its destination)
  * initial capacity of a new airport should be set to just 1 flight
  * other variables to help you maintain the information about the airport's flights.

**2. Constructor**

It should take the name of the airport as an input. Think of what the purpose of a constructor is!

**3. Instance methods**
* <code>addFlight()</code>: it takes a Flight object as input, and adds it to the array of Flights. If there is not enough space for a flight to be added, create a larger array.

* <code>toString()</code>: as usual, this method should provide a String representation of an object
of type Airport. This representation should contain the airport's name and capacity, the number
of flights it currently serves, as well as a listing of those flights.

* <code>deleteFlight()</code>: it takes a Flight object as input and removes this flight from the airport. Make sure that the resulting array of flights contains no "holes" after the removal of a flight.

* <code>findFlightsByAirline()</code>: takes as input the name of an airline, and returns an array with all the Flights of this airline that use this airport.

* <code>printFlightsByAirline()</code>: given the name of an airline,
it prints all the flights of this airline that are using this airport. While there are many ways to implement such a method, make sure your implementation uses the previous to compute the array of flights to print.

**4. No main() is required in the Airport class but create a separate client class**

Instead, create another client class called `LoganAirport.java`. This class contains only a <code>main()</code> method. It main purpose is to test your `Airport` class. Make sure you test your methods as you develop your code. Start by creating an instance of type <code>Airport</code> called `logan`, and some <code>Flight</code> instances.

* You can use the sample solutions provided here: [Flight.java](assign205/Flight.java)
 <br>If you would like to use your own Flight.java file, you can test it with our JUnit tester class found here: [FlightTest.java](assign205/FlightTest.java). To see that your code passes our tests, first save the tester class onto your computer. Then, drag and drop the tester class into the same project as your Flight code, compile, and control-click on it to choose "Test All".


**5. Write good javadoc**
Make sure you add nice javadoc to your code that includes:
* <code>above the class documentation</code> (but below any `import` statements): Provide a quick description of what this class is doing.
Use the <code> @author </code> and <code> @version </code> tags.

* <code> above a method documentation </code>: For every method provide a short
sentence to succinctly and accurately describe what this method is doing. Also, use the <code> @param </code> and <code> @return </code> javadoc tags as needed.

* <code> in-line comments </code>: Add them only as appropriately, to document your code. You should strike for a balance here: Ideally, the reader of your code should be able to follow it by just reading the comments. At  the same time, you should not document the obvious.

* Finally, take a look at the documentation automatically produced for your class in BlueJ, (click the Source Code button at the top right of the editing window and select Documentation) and examine it to make sure it is complete and reads well.

**6. Testing**

Save the printout of the `LoganAirport` class into a file named `LoganTesting.txt`. For inspiration look at our own [DriverTesting.txt](assign205/DriverTesting.txt) driver.


##Submitting your code
* Submit your `Airport.java`, your `LoganAirport.java`, your `LoganTesting.txt`, and your picture of your drawing of the class objects to Gradescope. 
* No need to upload the `Flight.java` code we linked above, unless it is your own `Flight.java` code (not our sample solutions from the previous assignment.) 

Remember that in Gradescope you have to upload all the files at once. Every submission you do overwrites the previous one, so if you upload one file at a time, only the last will be  saved.

Check your submission to make sure the right files have been submitted.

###Happy Coding!
