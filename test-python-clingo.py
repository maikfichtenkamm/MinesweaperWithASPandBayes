from clingo.control import Control

safes = []
def results(m):
    print(m)
    safes.append(str(m))


string1 = ""

ctl = Control(arguments=[f"--models=0"])

example = "uncovered(1,1). uncovered(1,0). assignment(1, 1, 1). assignment(1, 0, 1). totalmines(1). totalnotmines(5). totalcovered(2). numberCells(4). totaluncovered(2).#const r = 1.#const c = 1. "
ctl.add('base', [], example)
ctl.load("asp-v1-consistent-minefields.lp")
ctl.ground([("base", [])])
ctl.solve(on_model=results)
print(safes)