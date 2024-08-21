---
layout: default
---

# Homework 9, Part A: Graphs

## Learning Goals

* To understand Graphs and alternative implementations
* To understand and practice  basic graph traversal algorithms

**Note:** This exercise involves NO programming.


## Exercise: Working with Graphs

In this task you will work with an undirected Graph `G = {V, E}`, where `V = {f,p,s,b,l,j,t,c,d}` and `E = {(1,2), (1,3), (3,8), (4,8), (8,9), (1,7), (2,6), (2,3), (5,6), (6,7), (7,9), (8,1)}`.

Assume that the nodes are stored in an indexed linear structure (e.g., an array or a vector) numbered consecutively from 1 (node `f`) to 9 (node `d`).

### Task 1
Represent the graph `G` using the adjacency matrix representation. Draw this representation in your notebook or on your computer (using a drawing application).

### Task 2
Represent the graph `G` using the adjacency lists representation. Draw this representation in your notebook or on your computer (using a drawing application).

### Task 3
Type up a `tgf` representation of the graph `G` manually in a file, named `G.tgf`. Open that file in yEd and see the produced visualization of the graph. Arrange the nodes, on the yEd window, nicely so that the edges are not crossing. Try the various Layout options, including Orthogonal. Take a snapshot of that image.

### Task 4
Find a path from node `l` to node `b` with length 8, that passes through every vertex of the graph.
List the nodes of that path.

### Task 5
The graph `G` contains cycles. What is the smallest number of vertices to remove in order to break all cycles?

### Task 6
Run, by hand, a depth-first search (DFS) traversal of the graph `G`, starting at node  `p`. When choosing which node to visit next amongst the possibilities, choose the one that is next in alphabetical order. Give your answer by listing the edges in the order that DFS will select.


## Submitting your work

Submit one PDF file, named `GraphOnPaper.pdf` that contains your answers to all 6 questions, clearly marked: "Task 1 Answer" to "Task 6 Answer". Make sure the document you submit contains your name.







<br/>

# Homework 9, Part B: Maze

## Learning Goals

* To understand the correspondence between Graphs and Mazes
* To understand how a graph algorithm can solve a maze problem


**Note:** This exercise involves NO programming.

## Exercise: Solving a maze

Consider the following maze:

<img src="_images/figs/maze.png" />

Think about how you would model this maze as a graph so that you can employ graph traversal algorithms in order to solve it. By solving a maze we mean to have an algorithm that, entering from the top opening of the maze will exit at the bottom opening.

Some questions to consider:
1. How do you decide what is a vertex?
2. How do you decide what is an edge or an arc?
3. Show the data structure that represents the graph defined by the vertices and edges/arcs you chose.
4. Show the DFS and BFS traversals of the graph defined by your data structure
5. Which traversal is better? How did you decide?


## Submitting your work

Write up your answer on paper and take a photo of it. Submit one PDF file, named `MazeOnPaper.pdf` that contains your answers to all questions, clearly marked: "Task 1 Answer" to "Task 2 Answer", etc.

Make sure the document you submit contains your name.




