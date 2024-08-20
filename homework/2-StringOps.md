## FUN with Strings

###Goals:
1. to work with some of Java's built-in [String class](https://docs.oracle.com/javase/7/docs/api/java/lang/String.html) methods
2. to refresh your memory on recursion

### Task:

Create a new class named **StringOps** and include definitions for the following (static) methods:

 * **public static String removeChar(String str, char ch)**

 This method returns a string that is constructed from the input string **str**, with the first occurrence of the character **ch** removed from it. If the character **ch** is not contained in the input string **str**, then this method returns the original string.
 	 Examples:  
   * removeChar("java", 'q') returns "java"
   * removeChar("java", 'a') returns "jva"

 * **public static boolean testAnagrams(String word1, String word2)**

 It determines whether the two input strings **word1** and **word2** are anagrams. Returns true if the two
 input strings are anagrams, false otherwise. An **anagram** is defined as two words that have exactly the same letters, possibly in a different order.
 	Examples:
  * testAnagrams("melon", "lemon") returns true
  * testAnagrams("hello", "world") returns false
  * testAnagrams("hello", "hello") returns true (notice: a word is an anagram of itself)

 * **main()**

 As usual, it will contain your testing code. Make sure your testing is comprehensive, and your testing printing is informative, like in the following line:

 Calling testAnagrams(melon, lemon). Expect TRUE. Got: true

Save the results of your program into a textfile named `StringOpsTesting.txt`. You will need to submit this text file along with the source code.

  **Note**
You can assume that your input is all lowercase.
 
Both of the above methods have elegant solutions using recursion. We encourage you (but we do not require) to try to solve them with recursion.

### Submitting
When done, submit your <code>StringOps.java</code> along with the <code>StringOpsTesting.txt</code> that shows the results of your comprehensive testing. Please DO NOT submit any other file but these two.

 
 
 
