from pyamaze import maze, agent
m = maze(15,20)
m.CreateMaze()

a = agent(m, footprints=True, filled=True)
m.tracePath({a:m.path})
m.run()
