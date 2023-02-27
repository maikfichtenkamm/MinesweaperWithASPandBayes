
import numpy as np
import random
from clingo.control import Control

"""
class for applying ASP  to solve a Minesweeper Board
main function of the class is solve(), which returns the next moves
"""


class ASPSolver:
    def __init__(self, mode):
        """Initialization of the solver and important variables
        """
        self.shape = (8, 8)
        self.total_mines = 10
        self.own_implementation = True if mode == "own" else False
        # get all the cells of the board, compute only one time at the beginning
        self.all_cells = self.iterate_over_all_cells()
        # the current board configuration
        self.field = None
        # current number of not undiscovered mines
        # dictionary to get the neighbors of a cell
        self.cell_to_neighbor_dict = None
        # List of all current covered cells
        self.covered_cells = None
        # I reused some of the variables of the BayesSolver since they were useful also besides in a Bayesian Network
        # list of the current y variables, uncovered cells with covered cells as neighbors, for an detailed explaination y variables look at the report!
        self.y_variables_BN = None
        # list of the current x variables, covered cells next to uncovered cells, for an detailed explanation see report
        self.x_variables_BN = None
        # all 0 cells of the current board
        self.zero_cells = None
        # discovered mines being also an x variable
        self.x_variables_mines = None
        # dictionary with all Y variables as key: the values of each key are the X variables beeing neighbor to the corresponding key
        self.y_to_x_variables_BN = None

    def iterate_over_all_cells(self):
        """Returns all the cells as tuples of the beginner board
        """
        cells = []
        for i in range(0, 8):
            for j in range(0, 8):
                cells.append(tuple((i, j)))
        return cells

    def are_all_covered(self, field):
        """ See if the its the start of the game.
        This method was seen in the GitHub / Youtube of computersplaygame https://github.com/gamescomputersplay/minesweeper-solver/blob/main/minesweeper_game.py
        The code is published under the MIT License
        """
        for cell in self.all_cells:
            if field[cell] != -2:
                return False
        return True

    def generate_all_covered(self):
        ''' Generates all the covered cells and the zero cells of the current board
        '''
        all_covered = []
        all_zero_cells = []

        for cell in self.all_cells:
            if self.field[cell] == -2:
                all_covered.append(cell)
            if self.field[cell] == 0:
                all_zero_cells.append(cell)
        self.covered_cells = all_covered
        self.zero_cells = all_zero_cells

    def generate_variables(self):
        """ Generates important information and variables: 
        X_varibales: uncovered cells next to uncovered cells
        x_varibales_mines: X variables and marked as mines
        y_to_x_variables_BN: dict with keys of y variables and from their neighbors the important x variables
        """
        x_variables = set()
        x_variables_mines = set()
        y_to_x_variables_BN = {}

        # iterate through each y varibale
        for y_cells in self.y_variables_BN:
            y_to_x_set = []
            # gets the neighbor cells of the y variable
            for cell in self.cell_to_neighbor_dict[y_cells]:
                # if a cell is covered
                if cell in self.covered_cells:
                    # then there is a edge in the Bayesian network
                    x_variables.add(cell)
                    y_to_x_set.append(cell)
                # for mines in neighbors
                if self.field[cell] == -1:
                    # since we can add that knowledge into the Bayesian network
                    x_variables_mines.add(cell)
                    y_to_x_set.append(cell)
            # y_to_x_set can be empty -> dont add that Y Varibale!
            if y_to_x_set:
                y_to_x_variables_BN[y_cells] = y_to_x_set

        self.y_to_x_variables_BN = y_to_x_variables_BN
        self.x_variables_BN = x_variables
        self.x_variables_mines = x_variables_mines

    def generate_Ys_for_BN(self):
        """ Determines the Y variables
        """
        y_variales_BN = []
        for cell in self.all_cells:
            # Y varibles are uncovered
            if self.field[cell] >= 0:
                for covered_cell in self.covered_cells:
                    # each Y varible is only important if there is a covered cell as its neighbor
                    if abs(covered_cell[0] - cell[0]) <= 1 and abs(covered_cell[1] - cell[1]) <= 1:
                        y_variales_BN.append(cell)
                        break
        self.y_variables_BN = y_variales_BN

    def ground_string_dissertation(self):
        """Generates a logic program of the current available knowledge for the dissertation of Jörg Pührer Stepwise Debugging in
        Answer-Set Programming:Theoretical Foundations and Practical Realisation
        for a first impression, look at the file
        Returns:
            Returns a logic program in string form 
        """
        print("diss")

        result_string = ""
        # iterate through each cell
        for cell in self.all_cells:
            # if cell is uncovered and not a mine, it is a number according to the definition of the file.
            # a number is the coordinates of the cell and its number of mines in its neighbors
            if cell not in self.covered_cells and self.field[cell] != -1:
                t = cell + (self.field[cell],)
                t = str(t)
                result_string = result_string + f"number{t}. "
            else:
                # get the covered cells
                result_string = result_string + f"covered{cell}. "
        # last add the cells and the number of Mines, is always the same
        result_string = result_string + "cell(0..7, 0..7). nrOfMines(10)."
        return result_string

    def ground_string_own(self):
        """Generates a logic program of the current available knowledge for my own implementation for the Mainsweeper

        Returns:
            Returns a logic program in string form 
        """
        print("own")
        result_string = ""
        # iterate through each cell
        for cell in self.all_cells:
            if cell not in self.covered_cells and self.field[cell] != -1:
                # if a cell is not covered and not a mine, its a uncovered cell
                result_string = result_string + f"uncovered{cell}. "
                t = cell + (self.field[cell],)
                t = str(t)
                # an assignment is a cells coordinates and its state -> number of mines in its enighbors
                result_string = result_string + f"assignment{t}. "
            else:
                # get the covered cells
                result_string = result_string + f"covered{cell}. "

        totalcovered = len(self.covered_cells)
        # and the total amount of mines is important
        result_string = result_string + " totalmines(10)."
        return result_string

    def apply_asp(self):
        """Applies the choosen ASP to the given game situation

        Returns:
            The found safecells in an array
        """
        print("Beginn ASP")
        # get the correct asp file corresponding to the user input
        file = "asp-v4.lp" if self.own_implementation else "asp-dissertation.lp"
        extracted_safecells = []

        def results(m):
            """Extracts the safecells from the output of the clingo solver

            Args:
                Extracts the safecells of the clingo output and returns them in an array
            """
            extracted_safecells.append(str(m))
            print(str(m))
        # generate a logic program based on the current available knowledge of the game situation
        ground_string = self.ground_string_own(
        ) if self.own_implementation else self.ground_string_dissertation()
        # initialize the Control object for the grounding/solving process.
        print(ground_string)

        ctl = Control(arguments=[])

        # Extend the logic program
        ctl.add('base', [], ground_string)
        # Extend the logic program with a logic program in a file
        ctl.load(file)
        # Ground the given list of program parts specified by tuples of names and arguments.
        ctl.ground([("base", [])])
        # Starts a search.
        ctl.solve(on_model=results)
        safes = []
        # extract the safecells in tuple form to make a move
        for safecell in extracted_safecells:
            cell_arr = ()
            for c in safecell:
                if c.isdigit():
                    cell_arr = cell_arr + (int(c),)
            # Check for errors
            if len(cell_arr) == 2:
                safes.append(cell_arr)
        print("Finished ASP")
        return safes

    def dict_all_neighbors(self):
        ''' Generates the neighbors of all cells
        keys: (cell(j, i))
        values: a set of all neighorcells
        '''
        cell_to_neighbor = {}
        for i in range(self.shape[0]):  # 8
            for j in range(self.shape[1]):  # 8
                ys = set()
                for k in range(-1, 2):  # -1, 0, 1
                    for l in range(-1, 2):  # -1, 0, 1
                        # see if its a neighbor, and the cell is existing
                        if (abs(l)+abs(k) != 0) and i + k >= 0 and i + k <= 7 and j + l >= 0 and j + l <= 7:
                            ys.add(tuple((i+k, j+l)))
                cell_to_neighbor[tuple((i, j))] = ys
        self.cell_to_neighbor_dict = cell_to_neighbor

    def solve(self, field):
        """Main Method of the solver:

        Args:
            field: the current board situation

        Returns:
            two arrays: safecells and mines, can be empty
        """
        # first, get the current board and important information
        self.field = field
        self.generate_all_covered()
        # at the start of the game, make the first move!
        if self.are_all_covered(self.field):
            # starting at an edge leads to a higher winning rate
            return [(0, 0)], None

        # get the important information of a board situation
        self.dict_all_neighbors()
        self.generate_Ys_for_BN()
        self.generate_variables()

        # Basic Cases:
        safes = set()
        mines = set()
        # basic fall 1: see if a field has only mines in its neighbring covered cells
        for cell in self.y_variables_BN:
            if len(self.y_to_x_variables_BN[cell]) == field[cell]:
                for mine in self.y_to_x_variables_BN[cell]:
                    if mine not in self.x_variables_mines:
                        mines.add(mine)
                break
            # basic fall 2
            local_mines = 0
            # get the number of already known mines of a cells neighbors
            for mine in self.y_to_x_variables_BN[cell]:
                if mine in self.x_variables_mines:
                    local_mines += 1
            # if for a cell the position of all mines of its neighbors is known, all other mines of its neighbors must be safecells
            if field[cell] - local_mines == 0:
                for safecell in self.y_to_x_variables_BN[cell]:
                    if safecell not in self.x_variables_mines:
                        safes.add(safecell)

        # basic fall 2: if a cell is a zero cells
        for cell in self.zero_cells:
            for neighbor in self.cell_to_neighbor_dict[cell]:
                if neighbor in self.covered_cells:
                    safes.add(neighbor)

        if safes or mines:
            print("Basic fall")
            return list(safes), list(mines)

        # apply ASP logic
        safes = self.apply_asp()
        print("SAFES OF ASP", safes)
        if safes:
            print("ASP found safecells")
            return safes, mines
        else:
            print('Random Choice')
            # covered cells ohne die aufgedeckten
            return [random.choice(self.covered_cells)], None
