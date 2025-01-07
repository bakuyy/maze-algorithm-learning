from pyamaze import maze, agent
from queue import PriorityQueue

def h(cell1,cell2): # define the heuristic cost, which we use Manhattans distance
    x1,y1 = cell1
    x2,y2 = cell2
    return abs(x1-x2) + abs(y1-y2) 

def aStar(m):
    start = (m.rows, m.cols) # get starting cell at the bottom right
    g_score = {cell: float('inf')for cell in m.grid} # keep track of moves, starting at bottom right with 0 moves
    g_score[start] = 0
    f_score = {cell: float('inf') for cell in m.grid} # keep track of cost (g+h)(n), where it should start at max distance
    f_score[start] = h(start,(1,1))
    aPath = {}

    open = PriorityQueue() # initialize Priority queue
    open.put((h(start,(1,1)),h(start,(1,1)), start)) # parameters: (g+h)(n), h(n), start
    while not open.empty(): #while goal isn't reached yet or while it's not empty
        currCell = open.get()[2]
        # from the priority queue, we need the minimum cost on the basis of f(n), then on the basis of h(n)
        # #but we need cell value first (hence we index at 2)
        if currCell == (1,1):
            break
        for direction in "ESNW":
            if m.maze_map[currCell][direction] == True:
                if direction =="E":
                    childCell = (currCell[0], currCell[1]+1) 
                elif direction == "S":
                    childCell = (currCell[0]+1, currCell[1])
                elif direction == "N":  
                    childCell = (currCell[0]-1, currCell[1])
                elif direction == "W":
                    childCell = (currCell[0], currCell[1]-1)

                tempg_score = g_score[currCell] +1
                tempf_score = tempg_score + h(currCell, (1,1))

                if tempf_score < f_score[childCell]:
                    g_score[childCell] = tempg_score
                    f_score[childCell] = tempf_score
                    open.put((tempf_score, h(childCell,(1,1)), childCell))
                    aPath[childCell] = currCell

    # we will store it structured as: aPath[childCell] = currCell
    fwdPath = {}
    cell = (1,1)
    while cell != start:
        fwdPath[aPath[cell]] = cell
        cell = aPath[cell]

    return fwdPath


#will need m.rows, m.cols, m.grid, m.maze_map

if __name__== "__main__":
    m = maze(5,5)
    m.CreateMaze()
    path = aStar(m)
    a = agent(m,footprints=True)
    m.tracePath({a:path})

    m.run()
