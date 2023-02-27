cell(0..7, 0..7).
state(0..8). state(-1).
%1{assignment(X, Y, Z): state(Z)}1:- cell(X, Y).
%uncovered(X, Y) | covered(X, Y):- cell(X, Y).
mine(X, Y) | notmine(X, Y):- covered(X, Y).
%mine(X, Y):- assignment(X, Y, Z), state(Z), Z == -1.
%notmine(X,Y):- assignment(X,Y,Z),state(Z), Z >= 0.
% define the numbers of each
% from the answer set programing slides: slide 246
assignment(X, Y, -1):- mine(X, Y).
N{mine(X, Y): cell(X, Y)}N:- totalmines(N). 

1{assignment(X, Y, Z): state(Z)}1:- covered(X, Y).
%when mine, there is a negative assignment
falseass1:- mine(X, Y), assignment(X, Y, Z), Z != -1.
falseass2:- notmine(X, Y), assignment(X,Y,Z), Z == -1.

% calculate the neighorcells for each cell
equal_cells(X1, Y1, X2, Y2):- cell(X1, Y1), cell(X2, Y2), X1 == X2, Y1 == Y2.
neighbor(X1, Y1, X2, Y2):- cell(X1, Y1), cell(X2, Y2), |X1-X2| <= 1, |Y1-Y2| <= 1, not equal_cells(X1, Y1, X2, Y2).
neighbor(X1, Y1, X2, Y2):- neighbor(X2, Y2, X1, Y1).
1{safecell(X, Y): covered(X, Y), uncovered(A,B), neighbor(X,Y,A,B)}1.
%fulfilling requirements: around each assignment the number of mines is right!
compare(A, B, N):- N = #count{mine(X,Y):  neighbor(A,B,X,Y), mine(X, Y)}, cell(A,B).
falseass3:- assignment(A,B,Z), compare(A,B,N), Z != N, notmine(A, B).
falseass4:- assignment(A,B,Z), compare(A,B,N), Z != N, uncovered(A, B).
% state: -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8
% choice rule for the safecell
:- falseass1.
:- falseass2.
:- falseass3.
:- falseass4.
:- safecell(X, Y), mine(X, Y).
%:- not_neighbors_safecell_uncovered.
%c1:- assignment(X, Y, -1), not mine(X, Y).
%c2:- mine(X, Y), assignment(X, Y, Z), Z != -1.

%incorrectNumberOfMines:-  S = #count{mine(X, Y): neighbor(X1, Y1, X, Y)}, assignment(X1, Y1, Z), Z != S.
%:- incorrectNumberOfMines.

% if a field is not a mine, but a number -> number of mines is in neighbor
%Z {mine(X2, Y2): neighbor(X1, Y1, X2, Y2)} Z:- state(Z), assignment(X1, Y1, Z), Z >= -1.

#show safecell/2.




% may need to say a cell is covered or not. covered()