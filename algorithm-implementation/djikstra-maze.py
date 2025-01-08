from pyamaze import maze,agent, textLabel

# *h allows the function to accept a variable number of arguments after the first (m)
def djikstra(m, *h):

    hurdles = [(i.position, i.cost) for i in h]

    unvisited = {n: float('inf') for n in m.grid}
    unvisited[(m.rows, m.cols)] =0
    visited = {}

    revPath = {}

    while unvisited:
        currCell = min(unvisited,key=unvisited.get)
        visited[currCell] = unvisited[currCell]
        if currCell==(1,1):
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
                if childCell in visited:
                    continue
                tempDist = unvisited[currCell] +1

                for hurdle in hurdles: # add cost of hurdle to the curr cell (if it has one)
                    if hurdle[0] == currCell:
                        tempDist += hurdle[1]


                if tempDist<unvisited[childCell]:
                    unvisited[childCell] = tempDist
                    revPath[childCell] = currCell
        unvisited.pop(currCell)

    fwdPath = {}
    start=(m.rows,m.cols)
    cell = (1,1)
    while cell!=start:
        fwdPath[revPath[cell]]=cell
        cell=revPath[cell]
    return fwdPath, visited[(1,1)]



if __name__=="__main__":
    m = maze(6,6)
    m.CreateMaze(loopPercent=100)
    hurdle1 = agent(m,4,4,color="red")
    hurdle2 = agent(m,4,6,color="red")

    print(hurdle1.position)
    hurdle1.cost=100
    hurdle2.cost=100

    path,c = djikstra(m,hurdle1,hurdle2)
    textLabel(m,'Total Cost: ',c)
    a = agent(m, footprints=True)

    m.tracePath({a:path})

    m.run()