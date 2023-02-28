cell(0..7, 0..7).
state(0..8). state(-1).
mine(X, Y) | notmine(X, Y):- covered(X, Y).
assignment(X, Y, -1):- mine(X, Y).
N{mine(X, Y): cell(X, Y)}N:- totalmines(N). 

1{assignment(X, Y, Z): state(Z)}1:- covered(X, Y).
falseass1:- mine(X, Y), assignment(X, Y, Z), Z != -1.
falseass2:- notmine(X, Y), assignment(X,Y,Z), Z == -1.

% calculate the neighorcells for each cell
equal_cells(X1, Y1, X2, Y2):- cell(X1, Y1), cell(X2, Y2), X1 == X2, Y1 == Y2.
neighbor(X1, Y1, X2, Y2):- cell(X1, Y1), cell(X2, Y2), |X1-X2| <= 1, |Y1-Y2| <= 1, not equal_cells(X1, Y1, X2, Y2).
neighbor(X1, Y1, X2, Y2):- neighbor(X2, Y2, X1, Y1).
1{safecell(X, Y): covered(X, Y), uncovered(A,B), neighbor(X,Y,A,B)}1.
compare(A, B, N):- N = #count{mine(X,Y):  neighbor(A,B,X,Y), mine(X, Y)}, cell(A,B).
falseass3:- assignment(A,B,Z), compare(A,B,N), Z != N, notmine(A, B).
falseass4:- assignment(A,B,Z), compare(A,B,N), Z != N, uncovered(A, B).
:- falseass1.
:- falseass2.
:- falseass3.
:- falseass4.
:- safecell(X, Y), mine(X, Y).

#show safecell/2.
