Goals:

Implement one of the searching algorithms from the text.
Understand how an A.I. can find a solution to a problem through searching.
Understand how that solution can be used to influence an environment (in this case, the screen).
Jealous Husbands Implementation.

Write a program that finds a solution for the Jealous Husbands problem.

Your program should search through the state space searching for a solution.  If a solution is found, it should indicate the actions (in order) to get everyone across safely.  If no solution is possible, then the program should indicate no solution was found.

Output for your program could manifest in many ways, but it should be clear what is happening.

For example, one action in the solution output could be:     Wife from shore a to shore b.
Another action could be something like:      Husband and Wife from shore b to shore a.

It's up to you, but if the grader can't tell what's going on, you will not get credit.  Heck, if you are feeling adventurous, you could animate it using ASCII art or some other graphics.

Your program MUST be implemented using one of the uninformed search strategies covered in the text:  breadth-first search, uniform-cost search, depth-first search, depth-limited search, iterative deepening depth-first search, or bidirectional search.  Which one is up to you.  If this is not done, you will get no credit. 

Basically, implement one of the algorithms covered to find a solution.   Be sure to name the relevant parts as in the text.  That is, include the GOAL-TEST, ACTIONS, CHILD-NODE, SUCCESSOR functions as much as possible.  Where it's not possible, include in comments in your code what each section is doing.

For example:

// this method is generating all the possible actions

or

// this method creates the child node

We want to be able to tie your implementation to the algorithm visually as much as possible.

Note:  The solution for the search is an output of the search.  The solution is then used to generate the output shown on the screen.

<Initial State> ---->  [Search Algorithm]  ---> <Solution> ---> [Output Generator] ---> Screen

Find the solution, then use that solution to generate the output.  Don't try to display the output as the the solution is being searched for.  You'll probably get incorrect output that way. 

Get the solution, then use the solution to generate the output.
You may use whichever programming language you wish (Python, C++, Lisp, Java, C).

Include in comments at the top of your program which search algorithm you decided to use. 

Hints:

Don't forget that there is a ton of sample code provided by the author through their Git repository I showed you.  Feel free to base your solution on that. This could make the assignment super easy, barely an inconvenience.
Don't forget that the nodes being generated are being done dynamically.  The text implements data structures in a way that is probably different than you learned in your data structures class. 
Reminder:  I will not coauthor or debug your programs for you, but feel free to ask any questions you may have.
Make sure you understand the pseudocode for the algorithm you are implementing and the main components of it.  Ask if you are not sure.
This is your first "Major Programming Project".  You have 3 weeks to complete this.  Don't wait until the last minute to start it.  If you ask for an "extension", I'll feel bad for about 18 seconds and then say "no".  (although you can still turn it in a week late with a 30% penalty).
No.

Submission Instructions:

Submit your source code in a single file.
Include in the comments header how to run your program.
Do not upload screenshots.
Do not upload an executable.
Do not zip up your source code file or archive it in any way.
The grader should be able to download the file, read your comment header, and then run your program (compiling if necessary).
If you work with a group, each member must submit their own copy of the project and include the names of all group members in the submission comments.
