
# define our given graph using dictionary
'''
structure of our item is defined as 
{Node: {ConnectedNode:Cost,ConnectedNode:Cost}}

'''

def dijkstra(graph, start,goal): #can solve either entire graph or until the goal node:
    unvisited = {n:float('inf') for n in graph.keys()}
    unvisited[start]=0
    visited = {} # and the end, unvisited will be empty and visited will get final shortest cost of each node


    '''
    to keep track of the path from start -> goal
    we cannot have duplicate keys (or it will get overwritten), so we store it as neighbour as key and selected node as value

    '''
    revPath = {}


    while unvisited:
        minNode = min(unvisited, key=unvisited.get) # we want to choose the minimum based on the value of the key value pair
        # get will return all the values, and then we'll get the minimum

        visited[minNode] = unvisited[minNode] # this node is now "visited", assinged to the cost from above

        # finds path to target
        if minNode ==goal:
            break

        for neighbour in graph.get(minNode).keys(): # we check its connecting nodes
            if neighbour in visited: # we already visited this node
                continue
            tempDistance = unvisited[minNode] + graph[minNode][neighbour] #calculuate the distance
            if tempDistance<unvisited[neighbour]: # compare to see if this distance is smaller than previous smaller
                unvisited[neighbour] = tempDistance
                revPath[neighbour] = minNode
        unvisited.pop(minNode) 
        #remove this node from the unvisited dictionary as next iteration we must select the node w/minimum 
        #cost from remaining unvisited nodes
    
    # get path form start to goal
    node = goal
    revPathDirections = node
    while node!= start:
        revPathDirections += revPath[node]
        node = revPath[node]
    fwdPath = (revPathDirections)[::-1] # previously stored as reverse graph, so we have to reverse it
    print(fwdPath)
    return visited[goal]


myGraph={
    'A':{'B':2, 'C':9, 'F':4},
    'B':{'C':6, 'E':3, 'F':2},
    'C':{'D':1},
    'D':{'C':2},
    'E':{'D':5,'C':2},
    'F':{'E':3}
}

if __name__=="__main__":
    startNode = "A"
    target = "E"
    cost = dijkstra(myGraph,startNode,target)
    print(f'Cost is {cost}')