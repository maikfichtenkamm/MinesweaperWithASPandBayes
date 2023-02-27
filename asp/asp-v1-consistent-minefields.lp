uncovered(X, Y) | covered(X, Y):- cell(X, Y).
mine(X, Y) | notmine(X, Y):- covered(X, Y).
%mine(X, Y) | n_cell(X, Y):- cell(X, Y)
% state: -1, 0, 1, 2, 3, 4, 5, 6, 7, 8
state(0..8).state(-1).
% -1 == mine, -2 == Covered cell

% choices, X = row, Y = column, Z is the value of the neighboring mines
1 { assignment(X, Y, Z): state(Z) } 1 :- cell(X, Y).
%safecell(X, Y):- covered(X, Y), notmine(X, Y).

%:- totalmines(M), not #count{Z: assignment(X, Y, Z)} = M.
N {assignment(X, Y, -1): cell(X, Y)} N :- totalmines(N).

equal_cells(X1, Y1, X2, Y2):- cell(X1, Y1), cell(X2, Y2), X1 == X2, Y1 == Y2.
neighbor(X1, Y1, X2, Y2):- cell(X1, Y1), cell(X2, Y2), |X1-X2| <= 1, |Y1-Y2| <= 1, not equal_cells(X1, Y1, X2, Y2).
%X1 != X2 ? Y1 != Y2
% if a field is not a mine, but a number -> number of mines is in neighbor
Z {assignment(X2, Y2, -1): neighbor(X1, Y1, X2, Y2)} Z:- assignment(X1, Y1, Z), Z >= 0.

% from the answer set programing slides: slide 246
N{covered(X, Y): cell(X, Y)}N:- totalcovered(N). 
N{mine(X, Y): covered(X, Y)}N:- totalmines(N). 
%1{safecell(X, Y): covered(X, Y)}1. 

#show assignment/3.
% may need to say a cell is covered or not. covered()