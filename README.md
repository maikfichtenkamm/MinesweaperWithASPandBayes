# Project for the course Intro to Artificial Intelligence at the Alpen-Adria University of Klagenfurt

This project aims to develop a solver for the game Minesweeper. 
Two approaches were implemented: Bayesian Networks and Answer Set Programming with clingo. In addition, both contain a basic approach. This project was programmed in Python.
The solvers were tested on the free Minesweeper version Minesweeper X: http://www.curtisbright.com/msx/. 
The code to interact with this game was written by the Github account computersplaygames, which was published under the MIT License. This is located in the script minesweeper_bot.py.
The project aims at the beginner implementation of the game: a 8*8 board with 10 mines.
The solver can be started by starting the game Minesweeper X with all cells uncovered (Press F2).
Now the Minesweeper bot can be started, where you can choose between 3 arguments:

python minesweeper_bot.py -bs
python minesweeper_bot.py -asp-own
python minesweeper_bot.py -asp-dis

bs: Bayesian Network approach
asp-own: my own developed asp file
asp-dissertation: approach from the dissertation: Stepwise Debugging inAnswer-Set Programming:Theoretical Foundations and Practical Realisation by Jörg Pührer.

At the moment, I have not received a feedback for using the code of an dissertation. Therefore, the code for the last option is not published yet (the asp file).

## Scripts:

- asp_clingo_solver.py: consists of the Answer Set Programming solver
- bayes_solver: consists the Bayesian Network approach.
- asp folder: contains different logic programs. 
    - asp-v4.lp: my final version
- minesweeper_bot.py: interface to the Minesweeper X game
