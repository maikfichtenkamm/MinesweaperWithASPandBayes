# Projekt for the course Intro to Artificial Intelligence at the Alpen-Adria University of Klagenfurt

Dieses Porjekt zielte darauf ab einen Löser für das Spiel Minesweeper zu entwickeln. 
Dafür wurden zwei Ansätze implementiert: Bayesian Networks and Answer Set Programming with clingo. Zudem enthalten beide einen basic approach. Dieses Projekt wurde in Python programmiert.
Getested wurden die Löser an der kostenlosen Minesweeper Version Minesweeper X: http://www.curtisbright.com/msx/ 
Der Code um mit diesem SPiel zu interagieren wurde von dem Github Account computersplaygames geschrieben, welches unter der MIT License gepublished wurde. Dies befindet sich im Script minesweeper_bot.py
Das Projekt zielt auf die Beginner Implementation des Spieles ab: a 8*8 Board with 10 Mines.
Der Löser kann gestartet werden, indem das Spiel Minesweeper X gestartet wird, wobei alle Zellen uncovered sein sollen.
Nun wird der Minesweeper bot gestartet, woebi zwischen 3 argumenten gewählt werden kann:
python minesweeper_bot.py -bs
python minesweeper_bot.py -asp-own
python minesweeper_bot.py -asp-dis

## Scripts:

- asp_clingo_solver.py: consists of the Answer Set Programming solver
- bayes_solver: consists the Bayesian Network approach.
- asp folder: contains different logic programs. 
    - asp-v4.lp: my final version
- minesweeper_bot.py: interface to the Minesweeper X game
