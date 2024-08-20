# Hash it out

## Goals
* Better understanding of using a Hash Table
* Designing a program on your own



## Exercise: Use Hashtables to analyze word frequencies

In this exercise, you will use a hash table to count frequencies of words in some files.


###Task 1
To start, look at this [code](assign606/WordTable_Hash.java) and download the [DataFiles](assign606/DataFiles.zip) to use for testing your work. In that code, a hash table was used to count word frequencies in a single file. Go over the code, and make sure you understand it well before moving on. You should use parts of that code in the program you will write in the next step.

###Task 2
In this part, we will count word frequencies among multiple files, in particular all the files contained in a given directory (folder). The input of the program should be the name of a directory to be processed.
The output of the program should include:
* the total number of words read from **all files** in the given directory
* the number of distinct words in there, and
* the most frequent word among all files, together with its frequency.

You can iterate over the files in a directory like this:

```java
import java.io.File;

// args[0] is the name of a directory
dir= new File(args[0] + "/");
// dir points to the directory’s contents
File[]files= dir.listFiles();
System.out.println(files.length + "files");
for(File f:files) 
  if(!f.isHidden()) 
    process(f);
```    

The design of this program, i.e, what methods to have, what inputs they may take etc, is left up to you. As you design your application, remember some of the basic principals for writing code:
 * break your code into methods so that each method definition is not too long
 * code repetition (writing the some piece of code more than once) should be avoided
 * the main() method should be short, high-level and basically only call other methods
 * use descriptive names for methods, variables etc to improve the readability and the overall quality of your code

Download the folder [DataFiles](assign606/DataFiles.zip) to use for testing your work. Of course, feel free to use your own folder/files for testing purposes.

**Specifications:**
Please adhere to the following specifications:

* Name your program **WordFrequenciesDirectory_Hash.java**
* Your program should take the name of the folder to be processed as a **command line argument**. If no command line argument is provided by the user, the downloaded folder "DataFiles" should be used as input.
* Structure your output to look similar to this:

<pre>
Folder processed: DataFiles
Total number of words read: 1501990  
Number of distinct words: 60660
Most frequent word: the (frequency: 55965)
</pre>


###Task 3
Once you are done with the previous task, try to add some more functionality to your program:

Given a specific word, present the number of times it has repeated among all files in the directory processed by your program. Notice that it is left up to you how to get the "specific word" into your program.  Some ideas include:

* Hardwire it into your program
* Get it as (one more) command line argument
* Ask the user to type the word in the keyboard and read it into your program
* Perhaps, get in a dialogue with the user and allow them to enter, through the keyboard, more than
one such words.



###What to submit
 Submit to Gradescope your  **WordFrequenciesDirectory_Hash.java** and your **testing transcript**  (running your program on the DataFiles directory you downloaded).


Good luck!