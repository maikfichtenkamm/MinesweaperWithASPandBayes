
% establish neighbourhood and count covered
neighbour(X,Y,NX,NY) :- cell(X,Y),cell(NX,NY),|NX-X|<=1,|NY-Y|<=1,|NX-X|+|NY-Y|>=1.
potentialNrOfNeighbours(1..8).
nrCols(X) :- cell(X,Y),not cell(X+1,Y).
nrRows(Y) :- cell(X,Y),not cell(X,Y+1).
nrOfCells(X*Y) :- nrCols(X),nrRows(Y).
cellIndex(1..X) :- nrOfCells(X).
nrOfCovered(N) :- N={covered(X,Y):cell(X,Y)}.
nrOfCoveredNeighbours(X,Y,N) :- number(X,Y,_),N={covered(NX,NY):neighbour(X,Y,NX,NY)}.
% guess candidate
1{safeCell(X,Y):covered(X,Y)}1.
% guess mines
mine(X,Y) | empty(X,Y) :- covered(X,Y).
atLeastNCoveredNeighboursMines(X,Y,N) :- number(X,Y,_), potentialNrOfNeighbours(N), N {mine(NX,NY): neighbour(X,Y,NX,NY), covered(NX,NY)}.
atLeastNCoveredNeighboursFree(X,Y,N) :- number(X,Y,_), potentialNrOfNeighbours(N), N {empty(NX,NY): neighbour(X,Y,NX,NY), covered(NX,NY)}.
atLeastNCoveredMines(N) :- cellIndex(N), nrOfCovered(NC),N<=NC,N{mine(X,Y):covered(X,Y)}.
atLeastNCoveredFree(N) :- cellIndex(N), nrOfCovered(NC),N<=NC, N{empty(X,Y):covered(X,Y)}.
% spoiling conditions
spoil :- mine(X,Y),empty(X,Y).
spoil :- number(X,Y,N),atLeastNCoveredNeighboursMines(X,Y,N+1).
spoil :- number(X,Y,N),nrOfCoveredNeighbours(X,Y,NCN),atLeastNCoveredNeighboursFree(X,Y,(NCN-N)+1).
spoil :- nrOfMines(N),atLeastNCoveredMines(N+1).
spoil :- nrOfMines(N),nrOfCovered(NC),atLeastNCoveredFree((NC-N)+1).
spoil :- safeCell(X,Y), empty(X,Y).
% spoiling
mine(X,Y) :- covered(X,Y),spoil.
empty(X,Y) :- covered(X,Y),spoil.
:- not spoil.

#show safeCell/2.