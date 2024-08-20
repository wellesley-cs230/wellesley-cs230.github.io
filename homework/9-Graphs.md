
## Learning Goals

* To understand Graphs and alternative implementations
* To understand and practice  basic graph traversal algorithms


## Exercise: Working with Graphs

### This exercise involves NO programming.

In this task you will work with an undirected Graph `G = {V, E}`, where `V = {f,p,s,b,l,j,t,c,d}` and `E = {(1,2), (1,3), (3,8), (4,8), (8,9), (1,7), (2,6), (2,3), (5,6), (6,7), (7,9), (8,1)}`.

Assume that the nodes are stored in an indexed linear structure (e.g., an array or a vector) numbered consecutively from 1 (node `f`) to 9 (node `d`).

###Task 1
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

Submit one PDF file, named `GraphOnPaper.pdf` that contains your answers to all 6 questions, clearly marked: "Task 1 Answer" to "Task 6 Answer".

Make sure the document you submit contains your name.


**Good luck!**
