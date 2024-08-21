---
layout: default
---

# Homework 4, Part A: Airports

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


## Submitting your code
* Submit your `Airport.java`, your `LoganAirport.java`, your `LoganTesting.txt`, and your picture of your drawing of the class objects to Gradescope. 
* No need to upload the `Flight.java` code we linked above, unless it is your own `Flight.java` code (not our sample solutions from the previous assignment.) 

Remember that in Gradescope you have to upload all the files at once. Every submission you do overwrites the previous one, so if you upload one file at a time, only the last will be  saved.

Check your submission to make sure the right files have been submitted.

### Happy Coding!





# Homework 4, Part B: Deck

## Learning Goals
* Using arrays to hold and maintain collection of objects
* Using loops to process array elements


## Exercise:  Deck of Cards!

Create a class named <code>Deck</code> that creates a Deck of Card objects. 


### Specifications

For this exercise you are **NOT allowed to use any of Java's Arrays class**. Just use arrays of Objects as we did in lectures.

**0. Study and use the provided Card class.**
The [Card.java](assign207/Card.java) class is provided for you. Read it very carefully and provide documentation for all the methods. Pay close attention to the equals() method. 

Create a `Deck` class that contains the following:

Write **the @author and @version entries** in the top javadoc documentation now.
Without that, we will not grade your submission for this and all future assignments and labs.

**1.  Instance variables**

  * a counter to keep track of how many cards are in the Deck. 
  * a constant to keep track of the total number of cards in a full Deck (52)
  * an array to keep track of the collection of Cards in the Deck

**2. Constructor**

It should fill the array with all 52 unique possible Cards. 
Recall that a Card can have one of 4 possible suits and one of 13 possible values. 
You have complete freedom over how this can happen. 

**3. Instance methods**

* Start with <code>toString()</code>: as usual, this method should provide a neat String representation of an object of type Deck. 
This representation should print all the Cards in the Deck. 

* Instance method <code>cut()</code>. It picks at random a number between 1 and the number of cards in the Deck and it splits the deck in two piles. It then changes the order of these two piles in the Deck: the top pile goes to the bottom of the Deck. The Cards of the Deck remain the same but their order in the collection change to reflect the cut.
For example, if the cards were A,B,C,D,E and we randomly picked 2, the Deck is rearranged so that the cards appear in this order: C,D,E,A,B.

* Instance method <code>shuffle()</code>. It picks at random a card from the Deck and adds it to a new pile repeatedly until there are no cards left in the Deck. Then, the new pile becomes the collection of cards in the Deck. 

* Feel free to use any helper methods that you think are useful

**4. No main() is required in the Deck class**

Instead, create another client class called `Game.java`. This class contains only a <code>main()</code> method. It main purpose is to test your `Deck` class. Make sure you test your methods as you develop your code. 


**5. Write good javadoc**
Make sure you add nice javadoc to your code that includes:
* <code>above the class documentation</code> (but below any `import` statements): 
Provide a quick description of what this class is doing.
Use the <code> @author </code> and <code> @version </code> tags.

* <code>above a method documentation</code>: For every method provide a short
sentence to succinctly and accurately describe what this method is doing. 
Also, use the <code> @param </code> and <code> @return </code> javadoc tags as needed.

* <code> in-line comments </code> if needed: Add them only as appropriately, to document code that may be not easy to understand. You should strike for a balance here: Ideally, the reader of your code should be able to follow it by just reading the comments. 
At  the same time, you should not document the obvious.

* Finally, take a look at the documentation automatically produced for your class in BlueJ, (click the Source Code button at the top right of the editing window and select Documentation) and examine it to make sure it is complete and reads well.

**6. Testing**

Save the printout of the `Game` class into a file named `GameTesting.txt`. 

## Submitting your code
* Submit your commented `Card.java`, your `Deck.java`, your `Game.java`, and your `GameTesting.txt`, to Gradescope. 

Remember that in Gradescope you have to upload all the files at once. Every submission you do overwrites the previous one, so if you upload one file at a time, only the last will be  saved.

Check your submission to make sure the right files have been submitted.

### Happy Coding!

(Optional) If you would like to try JUnit, you can use this file: [DeckTest.java](assign207/DeckTest.java)
