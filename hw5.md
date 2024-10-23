---
layout: default
---


# Homework 5, Part A: Banks

## Learning Goals:
* Practice with the Java hierarchy through inheritance
* Practice with abstract classes and polymorphism
* Practice with designing a software solution based on provided specifications
* Learn to work with a *partner*


## Pair Assignments:

We will assign you a peer to collaborate with on this assignment. Please,
* Reach out to your partner ASAP to discuss when you will meet to work on the assignment. You will probably have to meet several times.
* Work *together* (pair programming) rather than *divide and conquer*.
* *Discuss* the ideas and diagrams before diving into coding.


## Specification

### How to start

As you can see, this is a long description. It likely requires a lot of thinking before one starts writing code, otherwise one risks the possibility of writing a lot of code that addresses a different set of specifications. 

We recommend that you start with keeping notes on paper and you draw the `UML diagram` of the classes you will need, along with their instance variables and their methods. Keep your UML diagram because you will need to submit it along with your code.


### Problem Description

Design and write the basic software that will manage bank accounts and their required functionality. Below are the requirements that were provided to you by the bank manager, a Wellesley graduate with CS230 experience (and a passion for creating classes through inheritance ;-)

According to the bank specifications, a client can **open** a new account in the bank. With every new account opened, the Bank produces a `unique` account number to associate with that new account. There are two types of accounts in the bank:

* A **`Checking Account`** has a **minimum balance** of $100, and an **overdraft fee** of $25. (The overdraft fee is a penalty that the Bank charges automatically if your balance falls under the minimum balance.) 
* A **`SavingsAccount`** has no minimum balance or overdraft fees. Every Savings account earns some **interest**, currently at an annual rate of 0.5%. The Bank calculates the earned interest and adds it to the balance on a monthly basis.

The following requirements must be implemented in your software:
* The two types of accounts have some attributes and behaviors in common. Think about how to use Java's inheritance model to design your application.
* A client can hold a **Checking Account** or a **Savings Account**, or both. No one can ever open just a plain Account!  
* **Depositing** money to an account functions exactly the same way for both kinds of accounts (Savings and Checking): the deposited amount is just added to the account's balance. This behavior can never be altered.
* **Withdrawing** an amount from either kind of account subtracts this amount from the account's balance. In general, for any type of account, attempts to withdraw an amount more than the account balance are simply denied.
* However, for checking accounts **ONLY**, *overdrafts* (i.e. withdraws resulting in a balance below the minimum balance, but not below zero) are allowed. Every overdraft results in the account being charged with an *overdraft fee*. At that point, the account balance can fall even below zero.
  > **Example:** Consider a checking account with balance of $200, minimum balance of $100 and overdraft fee of $25.
  > * A withdraw of $250 is ordered. The transaction is denied.
  > * A withdraw of $180 is ordered. The new balance would be $20, which is below the minimum balance. Therefore the overdraft fee of $25 is charged, which brings the account balance to $-5.

* Account owners should also be able to see a **display** of their account, including the kind of the account, the account number, its balance and other characteristics as appropriate (depending on the kind of the account).
* Finally, the **Bank** maintains a collection of accounts. It should be able to add directly an account to its collection, look for an account given its unique account number, print all accounts, and calculate all available funds (total of funds across all checking and saving accounts in the bank.)  



### Design and Implementation of the application

Read the problem description above and design your application code. You should have exactly 4 classes. Think about **inheritance** when designing those classes. Some of these classes share a lot of characteristics.

<!-- , Design and implement the following 4 classes:
1. `Account`,
2. `CheckingAccount`,
3. `SavingsAccount`, and
4. `Bank`

 the first three classes:
>A `CheckingAccount` **is-a** (special kind of an) `Account`.

> A `SavingsAccount` **is-a** (special kind of an )`Account`.

On the other hand, a `Bank` **contains** a collection of accounts.

Here is the diagram showing how these 4 classes relate. Pay attention to the kind of lines
connecting the different classes:

<img src="_images/figs/bankHierarchy.png" width = 400 alt="bank accounts hierarchy"> -->

To help you get started, here is a small description of one of the classes you should have in your application.

The `Account` class should contain all the common characteristics and functionality of any type of bank account. These include:
1. the -unique for each account- account number
2. the account balance
3. `deposit()`: a method for depositing an amount to the account
4. `withdraw()`: a method for withdrawing an amount from the account, and
5. `toString()`: a method to be used for printing the account.

Notes:
1. The `withdraw()` method behaves differently depending on the kind of the account. Therefore, think carefully: can you provide the definition for this method in the `Account` class? If not, where should it be defined?
2. The `toString()` method behaves almost the same in both types of accounts, but in the case of a *checking account* it should also include the minimum balance, while in the case of a *saving account* it should include the interest rate.
3. You can assume that the method to *accrue interest*, relevant only in Savings Accounts!, is called manually once a month; no need to keep track of dates. (Since the given interest rate is annual, make sure to calculate the monthly interest accordingly.)
4. An account cannot be removed from the `Bank` once it has been added, and the maximum number of accounts that a `Bank` can hold cannot change.


### Testing!

To show that your programs works correctly, you should create a `main()` method for each class that requires testing. Carefully think about what testing is relevant for each class. Your testing transcript should contain the correct/expected results next to the produced ones, so one can access correctness easier.

An example of running the Bank's main method is given in our below, wherein, in brackets [like this] is the explanation of the transaction that follows:

```text
Current state of Bank:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This bank currently manages 4 accounts: 
Checking  account num: 0	Balance: $1,000.00	Minimum balance: 100.0	Overdraft fee: 25
Savings   account num: 1	Balance: $1,000.00	Interest rate: 0.5
Checking  account num: 2	Balance: $500.00	Minimum balance: 100.0	Overdraft fee: 25
Savings   account num: 3	Balance: $500.00	Interest rate: 0.5
~~~~~~~~~~~~~~~~~~~~~~~~~~~ Total Funds: $3000.0

[Depositing $4000 into Checking #0. Should print Acct#0, Bal=$5000, Min=$100]
Checking  account num: 0	Balance: $5,000.00	Minimum balance: 100.0	Overdraft fee: 25

[Withdrawing $6K -- MORE THAN AVAILABLE from Checking #0]
** Withdrawal DENIED **: Insufficient balance.Checking  account num: 0	Balance: $5,000.00	Minimum balance: 100.0	Overdraft fee: 25

[Withdrawing $4901 from Checking #0 triggers Overdraft: Bal=$74.00]
** NOTE: Balance is low. Overdraft Fee was charged.
Checking  account num: 0	Balance: $74.00	Minimum balance: 100.0	Overdraft fee: 25

[Allowed Withdrawing $70 from Checking #0 triggers Overdraft: Bal=-$21.00]
** NOTE: Balance is low. Overdraft Fee was charged.
Checking  account num: 0	Balance: -$21.00	Minimum balance: 100.0	Overdraft fee: 25

[Withdrawing from NEGATIVE funds not allowed]
** Withdrawal DENIED **: Insufficient balance.Checking  account num: 0	Balance: -$21.00	Minimum balance: 100.0	Overdraft fee: 25

[Depositing $100 into Checking #0. Should print Acct#0, Bal=$79, Min=$100]
Checking  account num: 0	Balance: $79.00	Minimum balance: 100.0	Overdraft fee: 25

New state of Bank accounts:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This bank currently manages 4 accounts: 
Checking  account num: 0	Balance: $79.00	Minimum balance: 100.0	Overdraft fee: 25
Savings   account num: 1	Balance: $1,000.00	Interest rate: 0.5
Checking  account num: 2	Balance: $500.00	Minimum balance: 100.0	Overdraft fee: 25
Savings   account num: 3	Balance: $500.00	Interest rate: 0.5
~~~~~~~~~~~~~~~~~~~~~~~~~~~ Total Funds: $2079.0

[Depositing $2000 into Savings 1. Should print Acct#1, Bal=$3000, Int=0.5%]
Savings   account num: 1	Balance: $3,000.00	Interest rate: 0.5

[Withdrawing $5K MORE THAN AVAILABLE from Savings #1]
** Withdrawal DENIED **: Insufficient balance.
Savings   account num: 1	Balance: $3,000.00	Interest rate: 0.5

[Withdrawing $3K from Savings #1]
Savings   account num: 1	Balance: $0.00	Interest rate: 0.5
```



## What to submit

Your Gradescope submission should contain the following:

1. your <code>java</code> files
2. your corresponding <code>BankTesting.txt</code> files that contain your testing results
3. A PDF or PNG file of the UML diagram that corresponds to your solution.





<br/>

# Homework 5, Part B: Stacks

## Learning goals
* Get familiarity with Stacks
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

Please depict how your algorithm works graphically (by drawing it and taking a picture of it). You
will submit this at the end.  Make sure to include all relevant
information in this representation, so that a reader who is only
familiar with the Stack interface understands your approach.


### Specifications

* Your program should contain a **predicate** method `isPalindrome()` that returns true or false as appropriate.

* Your program should use Java's [Stack implementation](https://docs.oracle.com/javase/8/docs/api/java/util/Stack.html), relying only the stack methods `empty`, `peek`, `pop`, and `push`.

* Your `main()` method should test your code and show that it's correct.

* You can only use the `toCharArray()` method in the String class to
  convert the input string in an array of characters from which you
  will populate a stack. **You cannot not use any other String methods
  or array operations, other than indexing into an array and checking its length.**

* An input string is read as a `command-line argument` and is checked
  for the palindrome property. If there is no `args[0]` your program
  prints a message and continues execution (it does not crash). That
  way you can assign other strings as input and check for palindrome
  without having to re-run the program.

* Assume that the input string contains no spaces or special characters.

You are expected to **create your own test cases**, and demonstrate
that your code meets expectations. Remember that thorough testing
implies identifying and testing boundary cases as well.


* Optionally, you can get more practice by:
  * Create a JUnit testing file to test your design.
  * Describe at least 2 different ways of using two stacks to solve the problem. Which one is better? Why?


## What to submit

Submit 3 files: your `PalindromeChecker.java` file, the picture
describing your strategy in using stacks, and your testing `PalindromeChecker.txt`
file.



<br/>

# Submission Checklist

* You submitted **all** `.java` files and all `.txt` files.
* Your files are named **exactly** as in the homework specification, *including file extensions*.
* You tested **every possible** pathway in your code.
* You signed every class (or file) with `@author` and `@version`, accompanied by a description of what the class does.
* You wrote javadoc for every function, which includes `@param` and `@return`.
* You wrote inline comments explaining the logic of your code.
