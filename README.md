# Project for the course Intro to Artificial Intelligence at the Alpen-Adria University of Klagenfurt

This project aims to develop a solver for the game Minesweeper. 
Two approaches were implemented: Bayesian Networks and Answer Set Programming with clingo. In addition, both contain a basic approach. This project was programmed in Python.
The solvers were tested on the free Minesweeper version Minesweeper X: http://www.curtisbright.com/msx/. 
The code to interact with this game was written by the Github account computersplaygames, which was published under the MIT License. This is located in the script minesweeper_bot.py.
The project aims at the beginner implementation of the game: a 8*8 board with 10 mines.
The solver can be started by starting the game Minesweeper X with all cells uncovered (Press F2).
Now the Minesweeper bot can be started, where you can choose between 3 arguments:

- python minesweeper_bot.py -bs
- python minesweeper_bot.py -asp-own
- python minesweeper_bot.py -asp-dis

After that, you need to press F10 to start the Bot. The abbreviations stand for:
- bs: Bayesian Network approach
- asp-own: my own developed asp file
- asp-dissertation: approach from the dissertation: Stepwise Debugging inAnswer-Set Programming:Theoretical Foundations and Practical Realisation by Jörg Pührer.

At the moment, I have not received a feedback for using the code of an dissertation. Therefore, the code for the last option is not published yet (the asp file).

## Scripts:

- asp_clingo_solver.py: contains of the Answer Set Programming solver
- bayes_solver: contains the Bayesian Network approach.
- asp folder: contains different logic programs. 
    - asp-v4.lp: my final version
- minesweeper_bot.py: interface to the Minesweeper X game

## Installation
### Minesweeper X
Download the game Minesweeper X from http://www.curtisbright.com/msx/ and extract it. In Windows, the game can be started directly.
For Linux, you have to download wine and install necessary modules. Type into the console:
sudo apt-get install wine-stable
sudo apt-get install winetricks
winetricks vb6run
Now, the game can also be started: wine start path/to/exe

### Solver

For the Python script, I have added a requirement file:
    sudo pip install -r requirements.txt
The main problem is, that some of the modules need sudo rights. 

For me it had not worked to install the requirements in a virtual environment, because for example the module keyboard needs elevated rights. 
Therefore, you can also try to install the modules with:
    sudo pip install numpy==1.24.2 Pillow==9.4.0 PyAutoGUI==0.9.53 clingo==5.6.2 matplotlib pgmpy==0.1.21 keyboard==0.13.5

Also, it could be necessary to install scrot
    sudo apt-get install scrot

After that, it should be possible to run the Bot. For instance in Linux: sudo python3 minesweeper_bot.py -bs
