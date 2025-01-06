from pyamaze import maze, agent


def DFS(m):
    # bottom right grid (1-indexed)
    start = (m.rows, m.cols)

    # initialized stack and explored list
    explored = [start]
    frontier = [start]

    #hashmap to track paths
    dfsPath = {}

    #traverse the nodes
    while len(frontier) > 0:
        currCell = frontier.pop() # because of the last in first out principle of dfs
        if currCell == (1,1): # target grid
            break
        for direction in 'ESNW': # ESNW is reverse of priority queue (again bc of LIFO)
            if m.maze_map[currCell][direction] == True: #the following calculuates the adjacent direction agent should travel
                if direction =="E":
                    childCell = (currCell[0], currCell[1]+1) #i.e: east means you move one to the right
                elif direction == "S":
                    childCell = (currCell[0]+1, currCell[1]) # elif bc only one is valid at once (we test ESNW by looping through individually)
                elif direction == "N":  
                    childCell = (currCell[0]-1, currCell[1])
                elif direction == "W":
                    childCell = (currCell[0], currCell[1]-1)
                if childCell in explored: # skip over if its already been explored
                    continue
                frontier.append(childCell) # append to frontier bc its valid
                explored.append(childCell) # must add visited
                dfsPath[childCell] = currCell # add this step to the hashmap
                '''
                we keep track of childCell as key, since any given currCell can have more than one split, which would mean
                dfsPath[currCell]=childCell would yield duplicate keys
                '''

    fwdPath = {} #hashmap to track the valid path

    # goal coordinate
    cell=(1,1)

    # while we haven't reached the end, we're going to start at 1,1, and keep tracing the values to get the key, which is the next step
    while cell != start:
        fwdPath[dfsPath[cell]] = cell
        cell = dfsPath[cell]

    return fwdPath

if __name__ == '__main__':
    m = maze(5,5)
    m.CreateMaze()
    path = DFS(m)
    a = agent(m,footprints=True)
    m.tracePath({a:path})

    m.run()
